from __future__ import annotations

import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import audit_doc_language  # noqa: E402


def write_doc(tmp_dir: Path, text: str) -> Path:
    path = tmp_dir / "doc.md"
    path.write_text(text, encoding="utf-8")
    return path


class AuditDocLanguageTests(unittest.TestCase):
    def test_chinese_doc_with_technical_terms_passes(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            tmp_dir = Path(tmp)
            path = write_doc(
                tmp_dir,
                "# 当前状态\n\n使用 `docs/current/STATUS.md` 记录 Godot runtime 状态，路径和 API 名称不翻译。\n",
            )
            self.assertEqual(audit_doc_language.audit_file(path), [])

    def test_short_english_fragment_passes_default_mode(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            tmp_dir = Path(tmp)
            path = write_doc(tmp_dir, "# Runtime\n\nManual test scene: TBD\n")
            self.assertEqual(audit_doc_language.audit_file(path), [])

    def test_long_english_sentence_fails_default_mode(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            tmp_dir = Path(tmp)
            path = write_doc(
                tmp_dir,
                "this document explains how the gameplay validation process should be executed before every release candidate is accepted by the team.\n",
            )
            issues = audit_doc_language.audit_file(path)
            self.assertEqual(len(issues), 1)
            self.assertIn("English-looking sentence", issues[0])

    def test_consecutive_medium_english_lines_fail_default_mode(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            tmp_dir = Path(tmp)
            path = write_doc(
                tmp_dir,
                "\n".join(
                    [
                        "the validation flow should scan every output log.",
                        "the gameplay route should be checked by humans before acceptance.",
                        "the project state should be synchronized after acceptance every time.",
                    ]
                ),
            )
            issues = audit_doc_language.audit_file(path)
            self.assertEqual(len(issues), 1)
            self.assertIn("English-looking paragraph", issues[0])

    def test_code_block_is_ignored(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            tmp_dir = Path(tmp)
            path = write_doc(
                tmp_dir,
                "```md\nthis document explains how the gameplay validation process should be executed before release.\n```\n",
            )
            self.assertEqual(audit_doc_language.audit_file(path), [])

    def test_strict_mode_catches_shorter_english_heading(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            tmp_dir = Path(tmp)
            path = write_doc(tmp_dir, "# project workflow guide\n")
            self.assertEqual(audit_doc_language.audit_file(path), [])
            self.assertTrue(audit_doc_language.audit_file(path, strict=True))

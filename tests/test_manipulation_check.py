import pathlib


ROOT = pathlib.Path(__file__).resolve().parents[1]
HYPOTHESIS_SKILL = ROOT / "skills/hypothesis-testing/SKILL.md"
METHODOLOGY_SKILL = ROOT / "skills/research-methodology/SKILL.md"
MANIPULATION_CASE = (
    ROOT / "evals/test-cases/hypothesis-testing/test-manipulation-check.md")


def _section(text, start, end):
  return text[text.index(start):text.index(end)]


def test_manipulation_check_runs_after_variables_and_before_mitigation():
  skill = HYPOTHESIS_SKILL.read_text(encoding="utf-8")
  protocol = _section(skill, "<protocol>", "</protocol>")
  order = [
      "4. **Variable Specification**",
      "5. **Manipulation Check**",
      "6. **Mitigation Planning**",
      "7. **Falsification Criteria**",
  ]

  positions = [protocol.index(step) for step in order]
  assert positions == sorted(positions)


def test_manipulation_check_step_sets_a_floor_and_gates_null_results():
  skill = HYPOTHESIS_SKILL.read_text(encoding="utf-8")
  step = _section(skill, "5. **Manipulation Check**", "6. **Mitigation")

  assert "proxy" in step
  assert "pilot" in step
  assert "floor in the treatment arm" in step
  assert "cannot test the hypothesis" in step


def test_hypothesis_output_format_reports_the_manipulation_check():
  skill = HYPOTHESIS_SKILL.read_text(encoding="utf-8")

  assert "**Manipulation Check**" in _section(
      skill, "<output_format>", "</output_format>")


def test_methodology_quality_control_names_manipulation_validity():
  skill = METHODOLOGY_SKILL.read_text(encoding="utf-8")

  assert "manipulation" in _section(
      skill, "## 3. Validity & Quality Control", "## 4.").lower()


def test_manipulation_eval_case_targets_hypothesis_testing():
  case = MANIPULATION_CASE.read_text(encoding="utf-8")

  assert "- **Implementation Skill**: hypothesis-testing" in case
  assert "floor" in _section(case, "### Must Include", "### Should")

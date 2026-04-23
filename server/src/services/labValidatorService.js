const yaml = require('js-yaml');

function runValidation(lab, submittedCode) {
  const feedback = [];
  let totalPoints = 0;
  let earnedPoints = 0;

  let yamlValid = true;
  try { yaml.load(submittedCode); } catch(e) { yamlValid = false; }

  for (const rule of lab.validationRules) {
    totalPoints += rule.points;
    let passed = false;
    if (rule.type === 'contains') {
      passed = submittedCode.includes(rule.pattern);
    } else if (rule.type === 'not-contains') {
      passed = !submittedCode.includes(rule.pattern);
    } else if (rule.type === 'yamlParse') {
      passed = yamlValid;
    } else if (rule.type === 'regex') {
      passed = new RegExp(rule.pattern, rule.flags || '').test(submittedCode);
    }
    if (passed) earnedPoints += rule.points;
    else feedback.push({ ruleId: rule.id, message: rule.errorMessage });
  }

  const score = totalPoints > 0 ? Math.round((earnedPoints / totalPoints) * 100) : 0;
  const passed = score >= 70;
  const output = passed ? lab.simulatedOutput.success : lab.simulatedOutput.failure;
  return { passed, score, output, feedback };
}

module.exports = { runValidation };

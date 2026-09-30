import { n as require_jsx_runtime } from "../_libs/radix-ui__react-context+react.mjs";
import { n as QUESTIONS, o as useQuizStore, t as AppShell } from "./quiz-store-z9xPguVK.mjs";
import { t as QuestionPanel } from "./question-panel-BgVms2ql.mjs";
//#region node_modules/.nitro/vite/services/ssr/assets/praticar-ClVtC2sb.js
var import_jsx_runtime = require_jsx_runtime();
function Praticar() {
	const id = useQuizStore((s) => s.practiceIndex);
	const practice = useQuizStore((s) => s.practice);
	const selected = practice[id];
	const flagged = useQuizStore((s) => s.flagged.includes(id));
	const setPractice = useQuizStore((s) => s.setPractice);
	const setPracticeIndex = useQuizStore((s) => s.setPracticeIndex);
	const toggleFlag = useQuizStore((s) => s.toggleFlag);
	const go = (n) => setPracticeIndex(Math.min(QUESTIONS.length, Math.max(1, n)));
	return /* @__PURE__ */ (0, import_jsx_runtime.jsx)(AppShell, { children: /* @__PURE__ */ (0, import_jsx_runtime.jsx)(QuestionPanel, {
		id,
		selected,
		flagged,
		reveal: Boolean(selected),
		onSelect: (letter) => setPractice(id, letter),
		onFlag: () => toggleFlag(id),
		onPrev: () => go(id - 1),
		onNext: () => go(id + 1),
		onJump: go,
		answeredIds: Object.keys(practice).map(Number)
	}) });
}
//#endregion
export { Praticar as component };

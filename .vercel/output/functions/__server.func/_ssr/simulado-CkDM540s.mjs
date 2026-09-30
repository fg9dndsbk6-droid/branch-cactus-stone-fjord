import { x as useNavigate } from "../_libs/@tanstack/react-router+[...].mjs";
import { n as require_jsx_runtime } from "../_libs/radix-ui__react-context+react.mjs";
import { n as QUESTIONS, o as useQuizStore, t as AppShell } from "./quiz-store-z9xPguVK.mjs";
import { t as Button } from "./button-CILBH_Ek.mjs";
import { t as QuestionPanel } from "./question-panel-BgVms2ql.mjs";
//#region node_modules/.nitro/vite/services/ssr/assets/simulado-CkDM540s.js
var import_jsx_runtime = require_jsx_runtime();
function Simulado() {
	const navigate = useNavigate();
	const examStarted = useQuizStore((s) => s.examStarted);
	const examSubmitted = useQuizStore((s) => s.examSubmitted);
	const startExam = useQuizStore((s) => s.startExam);
	const submitExam = useQuizStore((s) => s.submitExam);
	const id = useQuizStore((s) => s.examIndex);
	const selected = useQuizStore((s) => s.exam[id]);
	const exam = useQuizStore((s) => s.exam);
	const flagged = useQuizStore((s) => s.flagged.includes(id));
	const setExam = useQuizStore((s) => s.setExam);
	const setExamIndex = useQuizStore((s) => s.setExamIndex);
	const toggleFlag = useQuizStore((s) => s.toggleFlag);
	const answered = Object.keys(exam).length;
	const go = (n) => setExamIndex(Math.min(QUESTIONS.length, Math.max(1, n)));
	if (examSubmitted) return /* @__PURE__ */ (0, import_jsx_runtime.jsx)(AppShell, { children: /* @__PURE__ */ (0, import_jsx_runtime.jsxs)("div", {
		className: "mx-auto max-w-lg rounded-xl border border-border bg-card p-8 text-center",
		children: [
			/* @__PURE__ */ (0, import_jsx_runtime.jsx)("h1", {
				className: "font-display text-3xl font-medium",
				children: "Simulado enviado"
			}),
			/* @__PURE__ */ (0, import_jsx_runtime.jsx)("p", {
				className: "mt-3 text-muted-foreground",
				children: "O gabarito está disponível na página de resultado, com comentário de cada item."
			}),
			/* @__PURE__ */ (0, import_jsx_runtime.jsx)(Button, {
				className: "mt-6",
				onClick: () => navigate({ to: "/resultado" }),
				children: "Ver resultado"
			})
		]
	}) });
	if (!examStarted) return /* @__PURE__ */ (0, import_jsx_runtime.jsx)(AppShell, { children: /* @__PURE__ */ (0, import_jsx_runtime.jsxs)("div", {
		className: "mx-auto max-w-lg rounded-xl border border-border bg-card p-8",
		children: [
			/* @__PURE__ */ (0, import_jsx_runtime.jsx)("p", {
				className: "text-sm font-medium uppercase tracking-[0.14em] text-steel",
				children: "Prova branca"
			}),
			/* @__PURE__ */ (0, import_jsx_runtime.jsx)("h1", {
				className: "mt-2 font-display text-3xl font-medium",
				children: "Simulado de 60 questões"
			}),
			/* @__PURE__ */ (0, import_jsx_runtime.jsx)("p", {
				className: "mt-4 leading-relaxed text-muted-foreground",
				children: "Sem gabarito até o fim. Marque uma alternativa por questão. Você pode voltar, pular e sinalizar itens para revisar. O progresso fica neste aparelho."
			}),
			/* @__PURE__ */ (0, import_jsx_runtime.jsxs)("ul", {
				className: "mt-5 list-disc space-y-1 pl-5 text-sm text-muted-foreground",
				children: [
					/* @__PURE__ */ (0, import_jsx_runtime.jsx)("li", { children: "Tempo sugerido: 90 a 120 minutos" }),
					/* @__PURE__ */ (0, import_jsx_runtime.jsx)("li", { children: "Uma resposta por questão" }),
					/* @__PURE__ */ (0, import_jsx_runtime.jsx)("li", { children: "Comentários só depois de enviar" })
				]
			}),
			/* @__PURE__ */ (0, import_jsx_runtime.jsx)(Button, {
				className: "mt-8 w-full sm:w-auto",
				size: "lg",
				onClick: startExam,
				children: "Começar agora"
			})
		]
	}) });
	return /* @__PURE__ */ (0, import_jsx_runtime.jsx)(AppShell, { children: /* @__PURE__ */ (0, import_jsx_runtime.jsx)(QuestionPanel, {
		id,
		selected,
		flagged,
		reveal: false,
		onSelect: (letter) => setExam(id, letter),
		onFlag: () => toggleFlag(id),
		onPrev: () => go(id - 1),
		onNext: () => go(id + 1),
		onJump: go,
		answeredIds: Object.keys(exam).map(Number),
		footer: /* @__PURE__ */ (0, import_jsx_runtime.jsxs)("div", {
			className: "flex flex-wrap items-center justify-between gap-3 rounded-xl border border-border bg-card px-4 py-4",
			children: [/* @__PURE__ */ (0, import_jsx_runtime.jsxs)("p", {
				className: "text-sm tabular-nums text-muted-foreground",
				children: [
					"Respondidas ",
					answered,
					" de ",
					QUESTIONS.length
				]
			}), /* @__PURE__ */ (0, import_jsx_runtime.jsx)(Button, {
				onClick: () => {
					submitExam();
					navigate({ to: "/resultado" });
				},
				children: "Enviar simulado"
			})]
		})
	}) });
}
//#endregion
export { Simulado as component };

import { i as __toESM } from "../_runtime.mjs";
import { n as require_react } from "../_libs/@radix-ui/react-compose-refs+[...].mjs";
import { b as Link } from "../_libs/@tanstack/react-router+[...].mjs";
import { n as require_jsx_runtime } from "../_libs/radix-ui__react-context+react.mjs";
import { a as ListChecks, d as ArrowRight, i as PenLine, o as FileDown, r as RotateCcw } from "../_libs/lucide-react.mjs";
import { n as QUESTIONS, o as useQuizStore, t as AppShell } from "./quiz-store-z9xPguVK.mjs";
import { t as Button } from "./button-CILBH_Ek.mjs";
//#region node_modules/.nitro/vite/services/ssr/assets/routes-JCPaUAXF.js
var import_react = /* @__PURE__ */ __toESM(require_react());
var import_jsx_runtime = require_jsx_runtime();
function useHydrated() {
	const [hydrated, setHydrated] = (0, import_react.useState)(false);
	(0, import_react.useEffect)(() => setHydrated(true), []);
	return hydrated;
}
function Home() {
	const hydrated = useHydrated();
	const practiceCount = Object.keys(useQuizStore((s) => s.practice)).length;
	const examCount = Object.keys(useQuizStore((s) => s.exam)).length;
	const examSubmitted = useQuizStore((s) => s.examSubmitted);
	const resetPractice = useQuizStore((s) => s.resetPractice);
	const resetExam = useQuizStore((s) => s.resetExam);
	const shownPractice = hydrated ? practiceCount : 0;
	const shownExam = hydrated ? examCount : 0;
	const shownSubmitted = hydrated && examSubmitted;
	return /* @__PURE__ */ (0, import_jsx_runtime.jsxs)(AppShell, { children: [
		/* @__PURE__ */ (0, import_jsx_runtime.jsxs)("section", {
			className: "grid gap-10 lg:grid-cols-[1.15fr_0.85fr] lg:items-end",
			children: [/* @__PURE__ */ (0, import_jsx_runtime.jsxs)("div", { children: [
				/* @__PURE__ */ (0, import_jsx_runtime.jsx)("p", {
					className: "text-sm font-medium uppercase tracking-[0.14em] text-steel",
					children: "Turma 78 · prova 1º de outubro"
				}),
				/* @__PURE__ */ (0, import_jsx_runtime.jsx)("h1", {
					className: "mt-3 max-w-xl font-display text-4xl font-semibold leading-[1.12] text-ink sm:text-5xl",
					children: "Identificar o estudo pela leitura."
				}),
				/* @__PURE__ */ (0, import_jsx_runtime.jsx)("p", {
					className: "mt-5 max-w-xl text-base leading-relaxed text-muted-foreground sm:text-lg",
					children: "Sessenta questões novas, no nível da prova do professor Cássio Zini. Só o material da Aula 6: característica, vantagem, desvantagem e exemplo. Gabarito embaralhado, quinze de cada letra."
				}),
				/* @__PURE__ */ (0, import_jsx_runtime.jsxs)("div", {
					className: "mt-8 flex flex-wrap gap-3",
					children: [/* @__PURE__ */ (0, import_jsx_runtime.jsx)(Button, {
						asChild: true,
						size: "lg",
						children: /* @__PURE__ */ (0, import_jsx_runtime.jsxs)(Link, {
							to: "/praticar",
							children: ["Praticar com gabarito ", /* @__PURE__ */ (0, import_jsx_runtime.jsx)(ArrowRight, {})]
						})
					}), /* @__PURE__ */ (0, import_jsx_runtime.jsx)(Button, {
						asChild: true,
						size: "lg",
						variant: "secondary",
						children: /* @__PURE__ */ (0, import_jsx_runtime.jsx)(Link, {
							to: "/simulado",
							children: "Fazer o simulado"
						})
					})]
				})
			] }), /* @__PURE__ */ (0, import_jsx_runtime.jsxs)("aside", {
				className: "rounded-xl border border-border bg-card p-6 sm:p-8",
				children: [/* @__PURE__ */ (0, import_jsx_runtime.jsxs)("dl", {
					className: "grid grid-cols-2 gap-6",
					children: [
						/* @__PURE__ */ (0, import_jsx_runtime.jsxs)("div", { children: [/* @__PURE__ */ (0, import_jsx_runtime.jsx)("dt", {
							className: "text-xs uppercase tracking-wider text-muted-foreground",
							children: "Questões"
						}), /* @__PURE__ */ (0, import_jsx_runtime.jsx)("dd", {
							className: "mt-1 font-display text-3xl font-medium tabular-nums",
							children: QUESTIONS.length
						})] }),
						/* @__PURE__ */ (0, import_jsx_runtime.jsxs)("div", { children: [/* @__PURE__ */ (0, import_jsx_runtime.jsx)("dt", {
							className: "text-xs uppercase tracking-wider text-muted-foreground",
							children: "Alternativas"
						}), /* @__PURE__ */ (0, import_jsx_runtime.jsx)("dd", {
							className: "mt-1 font-display text-3xl font-medium",
							children: "A–D"
						})] }),
						/* @__PURE__ */ (0, import_jsx_runtime.jsxs)("div", { children: [/* @__PURE__ */ (0, import_jsx_runtime.jsx)("dt", {
							className: "text-xs uppercase tracking-wider text-muted-foreground",
							children: "Prática"
						}), /* @__PURE__ */ (0, import_jsx_runtime.jsxs)("dd", {
							className: "mt-1 font-display text-3xl font-medium tabular-nums",
							children: [
								shownPractice,
								"/",
								QUESTIONS.length
							]
						})] }),
						/* @__PURE__ */ (0, import_jsx_runtime.jsxs)("div", { children: [/* @__PURE__ */ (0, import_jsx_runtime.jsx)("dt", {
							className: "text-xs uppercase tracking-wider text-muted-foreground",
							children: "Simulado"
						}), /* @__PURE__ */ (0, import_jsx_runtime.jsx)("dd", {
							className: "mt-1 font-display text-3xl font-medium tabular-nums",
							children: shownSubmitted ? "feito" : `${shownExam}/${QUESTIONS.length}`
						})] })
					]
				}), /* @__PURE__ */ (0, import_jsx_runtime.jsxs)("a", {
					href: "/simulado-epidemiologia.pdf",
					download: true,
					className: "mt-8 inline-flex h-11 items-center gap-2 text-sm font-medium text-steel hover:underline",
					children: [/* @__PURE__ */ (0, import_jsx_runtime.jsx)(FileDown, { className: "size-4" }), "Baixar a lista em PDF"]
				})]
			})]
		}),
		/* @__PURE__ */ (0, import_jsx_runtime.jsxs)("section", {
			className: "mt-12 grid gap-4 sm:grid-cols-3",
			children: [
				/* @__PURE__ */ (0, import_jsx_runtime.jsx)(ModeCard, {
					to: "/praticar",
					icon: /* @__PURE__ */ (0, import_jsx_runtime.jsx)(PenLine, { className: "size-4" }),
					title: "Praticar",
					copy: "Uma questão por vez, com comentário imediato ancorado na aula."
				}),
				/* @__PURE__ */ (0, import_jsx_runtime.jsx)(ModeCard, {
					to: "/simulado",
					icon: /* @__PURE__ */ (0, import_jsx_runtime.jsx)(ListChecks, { className: "size-4" }),
					title: "Simulado",
					copy: "As 60 questões sem gabarito. No fim, nota, temas e erros."
				}),
				/* @__PURE__ */ (0, import_jsx_runtime.jsx)(ModeCard, {
					to: "/revisao",
					icon: /* @__PURE__ */ (0, import_jsx_runtime.jsx)(RotateCcw, { className: "size-4" }),
					title: "Revisão",
					copy: "Filtre por tema, marcadas ou erradas. Leia o raciocínio de cada item."
				})
			]
		}),
		hydrated && (practiceCount > 0 || examCount > 0) && /* @__PURE__ */ (0, import_jsx_runtime.jsxs)("p", {
			className: "mt-10 flex flex-wrap gap-4 text-sm text-muted-foreground",
			children: [
				"Progresso guardado neste aparelho.",
				practiceCount > 0 ? /* @__PURE__ */ (0, import_jsx_runtime.jsx)("button", {
					type: "button",
					className: "text-steel underline-offset-4 hover:underline",
					onClick: resetPractice,
					children: "Zerar prática"
				}) : null,
				examCount > 0 ? /* @__PURE__ */ (0, import_jsx_runtime.jsx)("button", {
					type: "button",
					className: "text-steel underline-offset-4 hover:underline",
					onClick: resetExam,
					children: "Zerar simulado"
				}) : null
			]
		})
	] });
}
function ModeCard({ to, icon, title, copy }) {
	return /* @__PURE__ */ (0, import_jsx_runtime.jsxs)(Link, {
		to,
		className: "group flex flex-col rounded-xl border border-border bg-card p-5 transition-colors duration-[var(--motion-quick)] hover:bg-cream-deep sm:p-6",
		children: [
			/* @__PURE__ */ (0, import_jsx_runtime.jsx)("span", {
				className: "inline-flex size-9 items-center justify-center rounded-md bg-cream-deep text-steel group-hover:bg-background",
				children: icon
			}),
			/* @__PURE__ */ (0, import_jsx_runtime.jsx)("h2", {
				className: "mt-4 font-display text-xl font-medium",
				children: title
			}),
			/* @__PURE__ */ (0, import_jsx_runtime.jsx)("p", {
				className: "mt-2 flex-1 text-sm leading-relaxed text-muted-foreground",
				children: copy
			}),
			/* @__PURE__ */ (0, import_jsx_runtime.jsxs)("span", {
				className: "mt-4 inline-flex items-center gap-1 text-sm font-medium text-steel",
				children: ["Abrir ", /* @__PURE__ */ (0, import_jsx_runtime.jsx)(ArrowRight, { className: "size-3.5" })]
			})
		]
	});
}
//#endregion
export { Home as component };

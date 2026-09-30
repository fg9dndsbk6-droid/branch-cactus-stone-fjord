import { b as Link } from "../_libs/@tanstack/react-router+[...].mjs";
import { n as require_jsx_runtime } from "../_libs/radix-ui__react-context+react.mjs";
import { a as scoreOf, n as QUESTIONS, o as useQuizStore, t as AppShell } from "./quiz-store-z9xPguVK.mjs";
import { t as Button } from "./button-CILBH_Ek.mjs";
//#region node_modules/.nitro/vite/services/ssr/assets/resultado-CbyCdTVQ.js
var import_jsx_runtime = require_jsx_runtime();
function Resultado() {
	const exam = useQuizStore((s) => s.exam);
	const examSubmitted = useQuizStore((s) => s.examSubmitted);
	const startedAt = useQuizStore((s) => s.examStartedAt);
	const finishedAt = useQuizStore((s) => s.examFinishedAt);
	const resetExam = useQuizStore((s) => s.resetExam);
	if (!examSubmitted) return /* @__PURE__ */ (0, import_jsx_runtime.jsx)(AppShell, { children: /* @__PURE__ */ (0, import_jsx_runtime.jsxs)("div", {
		className: "mx-auto max-w-lg rounded-xl border border-border bg-card p-8 text-center",
		children: [
			/* @__PURE__ */ (0, import_jsx_runtime.jsx)("h1", {
				className: "font-display text-3xl font-medium",
				children: "Nenhum simulado enviado"
			}),
			/* @__PURE__ */ (0, import_jsx_runtime.jsx)("p", {
				className: "mt-3 text-muted-foreground",
				children: "Faça as 60 questões no modo simulado para ver a nota e o recorte por tema."
			}),
			/* @__PURE__ */ (0, import_jsx_runtime.jsx)(Button, {
				asChild: true,
				className: "mt-6",
				children: /* @__PURE__ */ (0, import_jsx_runtime.jsx)(Link, {
					to: "/simulado",
					children: "Ir ao simulado"
				})
			})
		]
	}) });
	const { correct, total, byTheme } = scoreOf(exam);
	const pct = Math.round(correct / total * 100);
	const minutes = startedAt && finishedAt ? Math.max(1, Math.round((finishedAt - startedAt) / 6e4)) : null;
	const misses = QUESTIONS.filter((q) => exam[q.id] && exam[q.id] !== q.answer);
	const blank = QUESTIONS.filter((q) => !exam[q.id]);
	return /* @__PURE__ */ (0, import_jsx_runtime.jsxs)(AppShell, { children: [
		/* @__PURE__ */ (0, import_jsx_runtime.jsxs)("header", {
			className: "mb-10",
			children: [
				/* @__PURE__ */ (0, import_jsx_runtime.jsx)("p", {
					className: "text-sm font-medium uppercase tracking-[0.14em] text-steel",
					children: "Resultado"
				}),
				/* @__PURE__ */ (0, import_jsx_runtime.jsxs)("h1", {
					className: "mt-2 font-display text-4xl font-medium tabular-nums",
					children: [
						correct,
						" / ",
						total,
						/* @__PURE__ */ (0, import_jsx_runtime.jsxs)("span", {
							className: "ml-3 text-2xl text-muted-foreground",
							children: [
								"(",
								pct,
								"%)"
							]
						})
					]
				}),
				/* @__PURE__ */ (0, import_jsx_runtime.jsxs)("p", {
					className: "mt-3 text-muted-foreground",
					children: [
						minutes ? `Tempo registrado: cerca de ${minutes} min. ` : null,
						blank.length ? `${blank.length} em branco. ` : "Todas as questões foram marcadas. ",
						"A prova cobra identificar o estudo — revise os erros pela característica, não pela letra."
					]
				}),
				/* @__PURE__ */ (0, import_jsx_runtime.jsxs)("div", {
					className: "mt-6 flex flex-wrap gap-3",
					children: [/* @__PURE__ */ (0, import_jsx_runtime.jsx)(Button, {
						asChild: true,
						children: /* @__PURE__ */ (0, import_jsx_runtime.jsx)(Link, {
							to: "/revisao",
							children: "Abrir revisão"
						})
					}), /* @__PURE__ */ (0, import_jsx_runtime.jsx)(Button, {
						variant: "secondary",
						onClick: () => {
							resetExam();
						},
						children: "Novo simulado"
					})]
				})
			]
		}),
		/* @__PURE__ */ (0, import_jsx_runtime.jsxs)("section", { children: [/* @__PURE__ */ (0, import_jsx_runtime.jsx)("h2", {
			className: "font-display text-xl font-medium",
			children: "Por tema"
		}), /* @__PURE__ */ (0, import_jsx_runtime.jsx)("ul", {
			className: "mt-4 divide-y divide-border rounded-xl border border-border bg-card",
			children: byTheme.map((row) => {
				const width = row.total ? row.correct / row.total * 100 : 0;
				return /* @__PURE__ */ (0, import_jsx_runtime.jsxs)("li", {
					className: "grid gap-2 px-4 py-3 sm:grid-cols-[1fr_120px] sm:items-center",
					children: [/* @__PURE__ */ (0, import_jsx_runtime.jsxs)("div", { children: [/* @__PURE__ */ (0, import_jsx_runtime.jsx)("p", {
						className: "text-sm font-medium",
						children: row.tema
					}), /* @__PURE__ */ (0, import_jsx_runtime.jsx)("div", {
						className: "mt-2 h-1.5 overflow-hidden rounded-full bg-cream-deep",
						children: /* @__PURE__ */ (0, import_jsx_runtime.jsx)("div", {
							className: "h-full bg-steel",
							style: { width: `${width}%` }
						})
					})] }), /* @__PURE__ */ (0, import_jsx_runtime.jsxs)("p", {
						className: "text-sm tabular-nums text-muted-foreground sm:text-right",
						children: [
							row.correct,
							"/",
							row.total
						]
					})]
				}, row.tema);
			})
		})] }),
		misses.length > 0 ? /* @__PURE__ */ (0, import_jsx_runtime.jsxs)("section", {
			className: "mt-10",
			children: [
				/* @__PURE__ */ (0, import_jsx_runtime.jsx)("h2", {
					className: "font-display text-xl font-medium",
					children: "Erros"
				}),
				/* @__PURE__ */ (0, import_jsx_runtime.jsx)("ul", {
					className: "mt-4 flex flex-col gap-2",
					children: misses.map((q) => /* @__PURE__ */ (0, import_jsx_runtime.jsxs)("li", {
						className: "rounded-lg border border-border bg-card px-4 py-3",
						children: [/* @__PURE__ */ (0, import_jsx_runtime.jsxs)("p", {
							className: "text-xs tabular-nums text-muted-foreground",
							children: [
								String(q.id).padStart(2, "0"),
								" · você marcou ",
								exam[q.id],
								" · gabarito ",
								q.answer
							]
						}), /* @__PURE__ */ (0, import_jsx_runtime.jsx)("p", {
							className: "mt-1 text-sm leading-snug",
							children: q.stem
						})]
					}, q.id))
				}),
				/* @__PURE__ */ (0, import_jsx_runtime.jsx)("p", {
					className: "mt-3 text-sm text-muted-foreground",
					children: "Os comentários completos estão em Revisão, filtro “Erradas”."
				})
			]
		}) : /* @__PURE__ */ (0, import_jsx_runtime.jsx)("p", {
			className: "mt-10 text-sm text-ok",
			children: "Nenhum erro registrado."
		})
	] });
}
//#endregion
export { Resultado as component };

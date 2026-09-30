import { n as require_jsx_runtime } from "../_libs/radix-ui__react-context+react.mjs";
import { c as ChevronLeft, l as Check, s as ChevronRight, t as X, u as Bookmark } from "../_libs/lucide-react.mjs";
import { i as cn, n as QUESTIONS } from "./quiz-store-z9xPguVK.mjs";
import { n as LETTERS, r as Badge } from "./router-EdH3eaw3.mjs";
import { t as Button } from "./button-CILBH_Ek.mjs";
import { n as Root, t as Indicator } from "../_libs/radix-ui__react-progress.mjs";
//#region node_modules/.nitro/vite/services/ssr/assets/question-panel-BgVms2ql.js
var import_jsx_runtime = require_jsx_runtime();
function Progress({ value, className }) {
	return /* @__PURE__ */ (0, import_jsx_runtime.jsx)(Root, {
		value,
		className: cn("relative h-1.5 w-full overflow-hidden rounded-full bg-cream-deep", className),
		children: /* @__PURE__ */ (0, import_jsx_runtime.jsx)(Indicator, {
			className: "h-full bg-primary transition-transform duration-[var(--motion-fast)] ease-[var(--ease-out)]",
			style: { transform: `translateX(-${100 - Math.min(100, Math.max(0, value))}%)` }
		})
	});
}
function QuestionPanel({ id, selected, flagged, reveal, onSelect, onFlag, onPrev, onNext, onJump, answeredIds, footer }) {
	const q = QUESTIONS[id - 1];
	if (!q) return null;
	const progress = id / QUESTIONS.length * 100;
	return /* @__PURE__ */ (0, import_jsx_runtime.jsxs)("article", {
		className: "flex flex-col gap-6",
		children: [
			/* @__PURE__ */ (0, import_jsx_runtime.jsxs)("div", {
				className: "flex flex-col gap-3",
				children: [/* @__PURE__ */ (0, import_jsx_runtime.jsxs)("div", {
					className: "flex items-center justify-between gap-3",
					children: [/* @__PURE__ */ (0, import_jsx_runtime.jsxs)("p", {
						className: "text-sm tabular-nums text-muted-foreground",
						children: [
							"Questão ",
							String(id).padStart(2, "0"),
							" de ",
							QUESTIONS.length
						]
					}), /* @__PURE__ */ (0, import_jsx_runtime.jsx)(Badge, { children: q.tema })]
				}), /* @__PURE__ */ (0, import_jsx_runtime.jsx)(Progress, { value: progress })]
			}),
			/* @__PURE__ */ (0, import_jsx_runtime.jsxs)("div", {
				className: "rounded-xl border border-border bg-card p-5 shadow-[0_1px_0_rgba(21,34,56,0.04)] sm:p-8",
				children: [
					/* @__PURE__ */ (0, import_jsx_runtime.jsx)("h1", {
						className: "font-display text-xl font-medium leading-snug text-ink sm:text-2xl",
						children: q.stem
					}),
					/* @__PURE__ */ (0, import_jsx_runtime.jsxs)("fieldset", {
						className: "mt-6 flex flex-col gap-3",
						"aria-label": "Alternativas",
						children: [/* @__PURE__ */ (0, import_jsx_runtime.jsx)("legend", {
							className: "sr-only",
							children: "Escolha uma alternativa"
						}), LETTERS.map((letter) => {
							const isSel = selected === letter;
							const isRight = q.answer === letter;
							const showOk = reveal && isRight;
							const showBad = reveal && isSel && !isRight;
							return /* @__PURE__ */ (0, import_jsx_runtime.jsxs)("button", {
								type: "button",
								onClick: () => onSelect(letter),
								className: cn("flex min-h-14 items-start gap-3 rounded-lg border px-4 py-3.5 text-left transition-colors duration-[var(--motion-quick)]", "focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring", showOk && "border-ok bg-ok-soft text-ink", showBad && "border-bad bg-bad-soft text-ink", !showOk && !showBad && isSel && "border-primary bg-cream-deep", !showOk && !showBad && !isSel && "border-border bg-card hover:bg-cream-deep"),
								children: [/* @__PURE__ */ (0, import_jsx_runtime.jsx)("span", {
									className: cn("mt-0.5 inline-flex size-7 shrink-0 items-center justify-center rounded-sm border text-sm font-semibold", showOk && "border-ok bg-ok text-primary-foreground", showBad && "border-bad bg-bad text-primary-foreground", !showOk && !showBad && "border-border bg-background text-steel"),
									children: showOk ? /* @__PURE__ */ (0, import_jsx_runtime.jsx)(Check, { className: "size-3.5" }) : showBad ? /* @__PURE__ */ (0, import_jsx_runtime.jsx)(X, { className: "size-3.5" }) : letter
								}), /* @__PURE__ */ (0, import_jsx_runtime.jsxs)("span", {
									className: "text-[15px] leading-relaxed sm:text-base",
									children: [/* @__PURE__ */ (0, import_jsx_runtime.jsxs)("span", {
										className: "sr-only",
										children: [letter, ") "]
									}), q.options[letter]]
								})]
							}, letter);
						})]
					}),
					reveal && selected ? /* @__PURE__ */ (0, import_jsx_runtime.jsxs)("div", {
						className: cn("mt-6 rounded-lg border px-4 py-4", selected === q.answer ? "border-ok/30 bg-ok-soft" : "border-bad/30 bg-bad-soft"),
						children: [/* @__PURE__ */ (0, import_jsx_runtime.jsxs)("p", {
							className: "text-sm font-semibold tracking-wide text-ink",
							children: [
								"Gabarito: ",
								q.answer,
								selected === q.answer ? " · correta" : " · sua marca estava em " + selected
							]
						}), /* @__PURE__ */ (0, import_jsx_runtime.jsx)("p", {
							className: "mt-2 text-[15px] leading-relaxed text-foreground",
							children: q.explain
						})]
					}) : null
				]
			}),
			/* @__PURE__ */ (0, import_jsx_runtime.jsxs)("div", {
				className: "flex flex-wrap items-center justify-between gap-3",
				children: [/* @__PURE__ */ (0, import_jsx_runtime.jsxs)(Button, {
					variant: "secondary",
					onClick: onPrev,
					disabled: id <= 1,
					children: [/* @__PURE__ */ (0, import_jsx_runtime.jsx)(ChevronLeft, {}), " Anterior"]
				}), /* @__PURE__ */ (0, import_jsx_runtime.jsxs)("div", {
					className: "flex items-center gap-2",
					children: [/* @__PURE__ */ (0, import_jsx_runtime.jsxs)(Button, {
						variant: flagged ? "default" : "outline",
						onClick: onFlag,
						"aria-pressed": flagged,
						children: [/* @__PURE__ */ (0, import_jsx_runtime.jsx)(Bookmark, { className: flagged ? "fill-current" : void 0 }), flagged ? "Marcada" : "Marcar"]
					}), /* @__PURE__ */ (0, import_jsx_runtime.jsxs)(Button, {
						onClick: onNext,
						disabled: id >= QUESTIONS.length,
						children: ["Próxima ", /* @__PURE__ */ (0, import_jsx_runtime.jsx)(ChevronRight, {})]
					})]
				})]
			}),
			onJump ? /* @__PURE__ */ (0, import_jsx_runtime.jsx)("ol", {
				className: "grid grid-cols-10 gap-1.5",
				children: QUESTIONS.map((item) => {
					const current = item.id === id;
					const answered = answeredIds?.includes(item.id);
					return /* @__PURE__ */ (0, import_jsx_runtime.jsx)("li", { children: /* @__PURE__ */ (0, import_jsx_runtime.jsx)("button", {
						type: "button",
						onClick: () => onJump(item.id),
						className: cn("flex h-9 w-full items-center justify-center rounded-sm text-xs tabular-nums", current ? "bg-primary text-primary-foreground" : answered ? "bg-steel/15 text-ink" : "bg-cream-deep text-muted-foreground hover:text-foreground"),
						"aria-label": `Ir para questão ${item.id}`,
						"aria-current": current ? "step" : void 0,
						children: item.id
					}) }, item.id);
				})
			}) : null,
			footer
		]
	});
}
//#endregion
export { QuestionPanel as t };

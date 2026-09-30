import { useMemo, useState } from "react";
import { createFileRoute } from "@tanstack/react-router";
import { AppShell } from "@/components/app-shell";
import { Badge } from "@/components/ui/badge";
import { QUESTIONS, THEMES } from "@/data/bank";
import { LETTERS, type Letter } from "@/data/types";
import { useQuizStore } from "@/lib/quiz-store";
import { cn } from "@/lib/utils";

export const Route = createFileRoute("/revisao")({ component: Revisao });

type Filter = "todas" | "marcadas" | "erradas" | "certas";

export function Revisao() {
  const [tema, setTema] = useState<string>("todos");
  const [filter, setFilter] = useState<Filter>("todas");
  const [open, setOpen] = useState<number | null>(null);
  const practice = useQuizStore((s) => s.practice);
  const exam = useQuizStore((s) => s.exam);
  const examSubmitted = useQuizStore((s) => s.examSubmitted);
  const flagged = useQuizStore((s) => s.flagged);

  const answers: Record<number, Letter> = examSubmitted ? exam : practice;

  const list = useMemo(() => {
    return QUESTIONS.filter((q) => {
      if (tema !== "todos" && q.tema !== tema) return false;
      const mark = answers[q.id];
      if (filter === "marcadas") return flagged.includes(q.id);
      if (filter === "erradas") return Boolean(mark) && mark !== q.answer;
      if (filter === "certas") return mark === q.answer;
      return true;
    });
  }, [tema, filter, answers, flagged]);

  return (
    <AppShell>
      <header className="mb-8">
        <h1 className="font-display text-3xl font-medium">Revisão comentada</h1>
        <p className="mt-2 max-w-2xl text-muted-foreground">
          O gabarito e o comentário de cada questão, só com o que a Aula 6 cobra.
          Filtre por tema ou pelo que você errou.
        </p>
      </header>

      <div className="mb-6 flex flex-col gap-3 sm:flex-row">
        <label className="flex min-w-0 flex-1 flex-col gap-1 text-xs font-medium uppercase tracking-wider text-muted-foreground">
          Tema
          <select
            className="h-11 rounded-md border border-border bg-card px-3 text-sm font-normal normal-case text-foreground"
            value={tema}
            onChange={(e) => setTema(e.target.value)}
          >
            <option value="todos">Todos os temas</option>
            {THEMES.map((t) => (
              <option key={t} value={t}>
                {t}
              </option>
            ))}
          </select>
        </label>
        <label className="flex flex-col gap-1 text-xs font-medium uppercase tracking-wider text-muted-foreground">
          Filtro
          <select
            className="h-11 rounded-md border border-border bg-card px-3 text-sm font-normal normal-case text-foreground"
            value={filter}
            onChange={(e) => setFilter(e.target.value as Filter)}
          >
            <option value="todas">Todas</option>
            <option value="marcadas">Marcadas</option>
            <option value="erradas">Erradas</option>
            <option value="certas">Certas</option>
          </select>
        </label>
      </div>

      <p className="mb-4 text-sm tabular-nums text-muted-foreground">
        {list.length} {list.length === 1 ? "questão" : "questões"}
      </p>

      <ul className="flex flex-col gap-3">
        {list.map((q) => {
          const expanded = open === q.id;
          const mark = answers[q.id];
          return (
            <li key={q.id} className="rounded-xl border border-border bg-card">
              <button
                type="button"
                className="flex w-full items-start justify-between gap-4 px-5 py-4 text-left"
                onClick={() => setOpen(expanded ? null : q.id)}
                aria-expanded={expanded}
              >
                <span>
                  <span className="text-xs tabular-nums text-muted-foreground">
                    Questão {String(q.id).padStart(2, "0")}
                  </span>
                  <span className="mt-1 block font-display text-lg font-medium leading-snug">
                    {q.stem}
                  </span>
                  <span className="mt-2 block">
                    <Badge>{q.tema}</Badge>
                  </span>
                </span>
                <span className="shrink-0 text-sm font-semibold text-steel">
                  {q.answer}
                </span>
              </button>
              {expanded ? (
                <div className="border-t border-border px-5 py-4">
                  <ul className="flex flex-col gap-2">
                    {LETTERS.map((letter) => (
                      <li
                        key={letter}
                        className={cn(
                          "rounded-md px-3 py-2 text-sm leading-relaxed",
                          letter === q.answer && "bg-ok-soft",
                          mark === letter && letter !== q.answer && "bg-bad-soft",
                        )}
                      >
                        <span className="font-semibold">{letter})</span> {q.options[letter]}
                      </li>
                    ))}
                  </ul>
                  <p className="mt-4 text-sm leading-relaxed text-foreground">{q.explain}</p>
                </div>
              ) : null}
            </li>
          );
        })}
      </ul>
    </AppShell>
  );
}

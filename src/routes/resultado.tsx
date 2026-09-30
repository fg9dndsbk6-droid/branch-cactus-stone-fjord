import { createFileRoute, Link } from "@tanstack/react-router";
import { AppShell } from "@/components/app-shell";
import { Button } from "@/components/ui/button";
import { QUESTIONS, scoreOf } from "@/data/bank";
import { useQuizStore } from "@/lib/quiz-store";

export const Route = createFileRoute("/resultado")({ component: Resultado });

function Resultado() {
  const exam = useQuizStore((s) => s.exam);
  const examSubmitted = useQuizStore((s) => s.examSubmitted);
  const startedAt = useQuizStore((s) => s.examStartedAt);
  const finishedAt = useQuizStore((s) => s.examFinishedAt);
  const resetExam = useQuizStore((s) => s.resetExam);

  if (!examSubmitted) {
    return (
      <AppShell>
        <div className="mx-auto max-w-lg rounded-xl border border-border bg-card p-8 text-center">
          <h1 className="font-display text-3xl font-medium">Nenhum simulado enviado</h1>
          <p className="mt-3 text-muted-foreground">
            Faça as 60 questões no modo simulado para ver a nota e o recorte por tema.
          </p>
          <Button asChild className="mt-6">
            <Link to="/simulado">Ir ao simulado</Link>
          </Button>
        </div>
      </AppShell>
    );
  }

  const { correct, total, byTheme } = scoreOf(exam);
  const pct = Math.round((correct / total) * 100);
  const minutes =
    startedAt && finishedAt ? Math.max(1, Math.round((finishedAt - startedAt) / 60000)) : null;
  const misses = QUESTIONS.filter((q) => exam[q.id] && exam[q.id] !== q.answer);
  const blank = QUESTIONS.filter((q) => !exam[q.id]);

  return (
    <AppShell>
      <header className="mb-10">
        <p className="text-sm font-medium uppercase tracking-[0.14em] text-steel">Resultado</p>
        <h1 className="mt-2 font-display text-4xl font-medium tabular-nums">
          {correct} / {total}
          <span className="ml-3 text-2xl text-muted-foreground">({pct}%)</span>
        </h1>
        <p className="mt-3 text-muted-foreground">
          {minutes ? `Tempo registrado: cerca de ${minutes} min. ` : null}
          {blank.length
            ? `${blank.length} em branco. `
            : "Todas as questões foram marcadas. "}
          A prova cobra identificar o estudo — revise os erros pela característica, não pela letra.
        </p>
        <div className="mt-6 flex flex-wrap gap-3">
          <Button asChild>
            <Link to="/revisao">Abrir revisão</Link>
          </Button>
          <Button
            variant="secondary"
            onClick={() => {
              resetExam();
            }}
          >
            Novo simulado
          </Button>
        </div>
      </header>

      <section>
        <h2 className="font-display text-xl font-medium">Por tema</h2>
        <ul className="mt-4 divide-y divide-border rounded-xl border border-border bg-card">
          {byTheme.map((row) => {
            const width = row.total ? (row.correct / row.total) * 100 : 0;
            return (
              <li key={row.tema} className="grid gap-2 px-4 py-3 sm:grid-cols-[1fr_120px] sm:items-center">
                <div>
                  <p className="text-sm font-medium">{row.tema}</p>
                  <div className="mt-2 h-1.5 overflow-hidden rounded-full bg-cream-deep">
                    <div
                      className="h-full bg-steel"
                      style={{ width: `${width}%` }}
                    />
                  </div>
                </div>
                <p className="text-sm tabular-nums text-muted-foreground sm:text-right">
                  {row.correct}/{row.total}
                </p>
              </li>
            );
          })}
        </ul>
      </section>

      {misses.length > 0 ? (
        <section className="mt-10">
          <h2 className="font-display text-xl font-medium">Erros</h2>
          <ul className="mt-4 flex flex-col gap-2">
            {misses.map((q) => (
              <li key={q.id} className="rounded-lg border border-border bg-card px-4 py-3">
                <p className="text-xs tabular-nums text-muted-foreground">
                  {String(q.id).padStart(2, "0")} · você marcou {exam[q.id]} · gabarito {q.answer}
                </p>
                <p className="mt-1 text-sm leading-snug">{q.stem}</p>
              </li>
            ))}
          </ul>
          <p className="mt-3 text-sm text-muted-foreground">
            Os comentários completos estão em Revisão, filtro “Erradas”.
          </p>
        </section>
      ) : (
        <p className="mt-10 text-sm text-ok">Nenhum erro registrado.</p>
      )}
    </AppShell>
  );
}

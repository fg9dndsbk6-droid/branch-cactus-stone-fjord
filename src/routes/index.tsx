import type { ReactNode } from "react";
import { createFileRoute, Link } from "@tanstack/react-router";
import { ArrowRight, FileDown, ListChecks, PenLine, RotateCcw } from "lucide-react";
import { AppShell } from "@/components/app-shell";
import { Button } from "@/components/ui/button";
import { QUESTIONS } from "@/data/bank";
import { useQuizStore } from "@/lib/quiz-store";
import { useHydrated } from "@/lib/use-hydrated";

export const Route = createFileRoute("/")({ component: Home });

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

  return (
    <AppShell>
      <section className="grid gap-10 lg:grid-cols-[1.15fr_0.85fr] lg:items-end">
        <div>
          <p className="text-sm font-medium uppercase tracking-[0.14em] text-steel">
            Turma 78 · prova 1º de outubro
          </p>
          <h1 className="mt-3 max-w-xl font-display text-4xl font-semibold leading-[1.12] text-ink sm:text-5xl">
            Identificar o estudo pela leitura.
          </h1>
          <p className="mt-5 max-w-xl text-base leading-relaxed text-muted-foreground sm:text-lg">
            Sessenta questões novas, no nível da prova do professor Cássio Zini.
            Só o material da Aula 6: característica, vantagem, desvantagem e
            exemplo. Gabarito embaralhado, quinze de cada letra.
          </p>
          <div className="mt-8 flex flex-wrap gap-3">
            <Button asChild size="lg">
              <Link to="/praticar">
                Praticar com gabarito <ArrowRight />
              </Link>
            </Button>
            <Button asChild size="lg" variant="secondary">
              <Link to="/simulado">Fazer o simulado</Link>
            </Button>
          </div>
        </div>
        <aside className="rounded-xl border border-border bg-card p-6 sm:p-8">
          <dl className="grid grid-cols-2 gap-6">
            <div>
              <dt className="text-xs uppercase tracking-wider text-muted-foreground">
                Questões
              </dt>
              <dd className="mt-1 font-display text-3xl font-medium tabular-nums">
                {QUESTIONS.length}
              </dd>
            </div>
            <div>
              <dt className="text-xs uppercase tracking-wider text-muted-foreground">
                Alternativas
              </dt>
              <dd className="mt-1 font-display text-3xl font-medium">A–D</dd>
            </div>
            <div>
              <dt className="text-xs uppercase tracking-wider text-muted-foreground">
                Prática
              </dt>
              <dd className="mt-1 font-display text-3xl font-medium tabular-nums">
                {shownPractice}/{QUESTIONS.length}
              </dd>
            </div>
            <div>
              <dt className="text-xs uppercase tracking-wider text-muted-foreground">
                Simulado
              </dt>
              <dd className="mt-1 font-display text-3xl font-medium tabular-nums">
                {shownSubmitted ? "feito" : `${shownExam}/${QUESTIONS.length}`}
              </dd>
            </div>
          </dl>
          <a
            href="/simulado-epidemiologia.pdf"
            download
            className="mt-8 inline-flex h-11 items-center gap-2 text-sm font-medium text-steel hover:underline"
          >
            <FileDown className="size-4" />
            Baixar a lista em PDF
          </a>
        </aside>
      </section>

      <section className="mt-12 grid gap-4 sm:grid-cols-3">
        <ModeCard
          to="/praticar"
          icon={<PenLine className="size-4" />}
          title="Praticar"
          copy="Uma questão por vez, com comentário imediato ancorado na aula."
        />
        <ModeCard
          to="/simulado"
          icon={<ListChecks className="size-4" />}
          title="Simulado"
          copy="As 60 questões sem gabarito. No fim, nota, temas e erros."
        />
        <ModeCard
          to="/revisao"
          icon={<RotateCcw className="size-4" />}
          title="Revisão"
          copy="Filtre por tema, marcadas ou erradas. Leia o raciocínio de cada item."
        />
      </section>

      {hydrated && (practiceCount > 0 || examCount > 0) && (
        <p className="mt-10 flex flex-wrap gap-4 text-sm text-muted-foreground">
          Progresso guardado neste aparelho.
          {practiceCount > 0 ? (
            <button type="button" className="text-steel underline-offset-4 hover:underline" onClick={resetPractice}>
              Zerar prática
            </button>
          ) : null}
          {examCount > 0 ? (
            <button type="button" className="text-steel underline-offset-4 hover:underline" onClick={resetExam}>
              Zerar simulado
            </button>
          ) : null}
        </p>
      )}
    </AppShell>
  );
}

function ModeCard({
  to,
  icon,
  title,
  copy,
}: {
  to: "/praticar" | "/simulado" | "/revisao";
  icon: ReactNode;
  title: string;
  copy: string;
}) {
  return (
    <Link
      to={to}
      className="group flex flex-col rounded-xl border border-border bg-card p-5 transition-colors duration-[var(--motion-quick)] hover:bg-cream-deep sm:p-6"
    >
      <span className="inline-flex size-9 items-center justify-center rounded-md bg-cream-deep text-steel group-hover:bg-background">
        {icon}
      </span>
      <h2 className="mt-4 font-display text-xl font-medium">{title}</h2>
      <p className="mt-2 flex-1 text-sm leading-relaxed text-muted-foreground">{copy}</p>
      <span className="mt-4 inline-flex items-center gap-1 text-sm font-medium text-steel">
        Abrir <ArrowRight className="size-3.5" />
      </span>
    </Link>
  );
}

import { createFileRoute, useNavigate } from "@tanstack/react-router";
import { AppShell } from "@/components/app-shell";
import { QuestionPanel } from "@/components/question-panel";
import { Button } from "@/components/ui/button";
import { QUESTIONS } from "@/data/bank";
import { useQuizStore } from "@/lib/quiz-store";

export const Route = createFileRoute("/simulado")({ component: Simulado });

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

  const go = (n: number) => setExamIndex(Math.min(QUESTIONS.length, Math.max(1, n)));

  if (examSubmitted) {
    return (
      <AppShell>
        <div className="mx-auto max-w-lg rounded-xl border border-border bg-card p-8 text-center">
          <h1 className="font-display text-3xl font-medium">Simulado enviado</h1>
          <p className="mt-3 text-muted-foreground">
            O gabarito está disponível na página de resultado, com comentário de cada item.
          </p>
          <Button className="mt-6" onClick={() => navigate({ to: "/resultado" })}>
            Ver resultado
          </Button>
        </div>
      </AppShell>
    );
  }

  if (!examStarted) {
    return (
      <AppShell>
        <div className="mx-auto max-w-lg rounded-xl border border-border bg-card p-8">
          <p className="text-sm font-medium uppercase tracking-[0.14em] text-steel">
            Prova branca
          </p>
          <h1 className="mt-2 font-display text-3xl font-medium">Simulado de 60 questões</h1>
          <p className="mt-4 leading-relaxed text-muted-foreground">
            Sem gabarito até o fim. Marque uma alternativa por questão. Você pode voltar,
            pular e sinalizar itens para revisar. O progresso fica neste aparelho.
          </p>
          <ul className="mt-5 list-disc space-y-1 pl-5 text-sm text-muted-foreground">
            <li>Tempo sugerido: 90 a 120 minutos</li>
            <li>Uma resposta por questão</li>
            <li>Comentários só depois de enviar</li>
          </ul>
          <Button className="mt-8 w-full sm:w-auto" size="lg" onClick={startExam}>
            Começar agora
          </Button>
        </div>
      </AppShell>
    );
  }

  return (
    <AppShell>
      <QuestionPanel
        id={id}
        selected={selected}
        flagged={flagged}
        reveal={false}
        onSelect={(letter) => setExam(id, letter)}
        onFlag={() => toggleFlag(id)}
        onPrev={() => go(id - 1)}
        onNext={() => go(id + 1)}
        onJump={go}
        answeredIds={Object.keys(exam).map(Number)}
        footer={
          <div className="flex flex-wrap items-center justify-between gap-3 rounded-xl border border-border bg-card px-4 py-4">
            <p className="text-sm tabular-nums text-muted-foreground">
              Respondidas {answered} de {QUESTIONS.length}
            </p>
            <Button
              onClick={() => {
                submitExam();
                void navigate({ to: "/resultado" });
              }}
            >
              Enviar simulado
            </Button>
          </div>
        }
      />
    </AppShell>
  );
}

import { createFileRoute } from "@tanstack/react-router";
import { AppShell } from "@/components/app-shell";
import { QuestionPanel } from "@/components/question-panel";
import { QUESTIONS } from "@/data/bank";
import { useQuizStore } from "@/lib/quiz-store";

export const Route = createFileRoute("/praticar")({ component: Praticar });

function Praticar() {
  const id = useQuizStore((s) => s.practiceIndex);
  const practice = useQuizStore((s) => s.practice);
  const selected = practice[id];
  const flagged = useQuizStore((s) => s.flagged.includes(id));
  const setPractice = useQuizStore((s) => s.setPractice);
  const setPracticeIndex = useQuizStore((s) => s.setPracticeIndex);
  const toggleFlag = useQuizStore((s) => s.toggleFlag);

  const go = (n: number) => setPracticeIndex(Math.min(QUESTIONS.length, Math.max(1, n)));

  return (
    <AppShell>
      <QuestionPanel
        id={id}
        selected={selected}
        flagged={flagged}
        reveal={Boolean(selected)}
        onSelect={(letter) => setPractice(id, letter)}
        onFlag={() => toggleFlag(id)}
        onPrev={() => go(id - 1)}
        onNext={() => go(id + 1)}
        onJump={go}
        answeredIds={Object.keys(practice).map(Number)}
      />
    </AppShell>
  );
}

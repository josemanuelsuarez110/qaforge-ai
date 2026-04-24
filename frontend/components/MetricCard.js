"use client";

export default function MetricCard({ title, value, delta, icon: Icon }) {
  return (
    <div className="rounded-3xl border border-slate-700 bg-slate-900/80 p-6 shadow-xl shadow-slate-900/30">
      <div className="flex items-center justify-between gap-3">
        <div>
          <p className="text-sm uppercase tracking-[0.24em] text-slate-400">{title}</p>
          <p className="mt-3 text-3xl font-semibold text-white">{value}</p>
        </div>
        <div className="inline-flex h-12 w-12 items-center justify-center rounded-2xl bg-slate-800 text-blue-400">
          <Icon className="h-6 w-6" />
        </div>
      </div>
      {delta ? (
        <p className="mt-4 text-sm text-slate-300">{delta}</p>
      ) : null}
    </div>
  );
}

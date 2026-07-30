import React from 'react';
import data from './data.json';

export default function FinancialDashboard() {
  return (
    <div className="min-h-screen bg-slate-900 text-slate-100 p-8 font-sans">
      {/* Encabezado */}
      <header className="mb-8 border-b border-slate-700 pb-4">
        <span className="text-xs uppercase tracking-widest text-rose-400 font-semibold">{data.sector}</span>
        <h1 className="text-3xl font-bold text-white mt-1">{data.empresa}</h1>
        <p className="text-slate-400 text-sm mt-2 max-w-3xl">{data.desafio}</p>
      </header>

      {/* Tarjetas de Métricas Clave (Ingeniería Económica) */}
      <section className="grid grid-cols-1 md:grid-cols-4 gap-4 mb-8">
        <div className="bg-slate-800 p-5 rounded-xl border border-slate-700">
          <span className="text-slate-400 text-xs uppercase font-medium">Valor Actual Neto (VAN)</span>
          <p className="text-2xl font-bold text-emerald-400 mt-1">${data.metricas_clave.van_usd.toLocaleString()} USD</p>
        </div>
        <div className="bg-slate-800 p-5 rounded-xl border border-slate-700">
          <span className="text-slate-400 text-xs uppercase font-medium">Tasa Interna de Retorno (TIR)</span>
          <p className="text-2xl font-bold text-blue-400 mt-1">{data.metricas_clave.tir_porcentaje}%</p>
        </div>
        <div className="bg-slate-800 p-5 rounded-xl border border-slate-700">
          <span className="text-slate-400 text-xs uppercase font-medium">Costo de Capital (WACC)</span>
          <p className="text-2xl font-bold text-amber-400 mt-1">{data.metricas_clave.wacc_porcentaje}%</p>
        </div>
        <div className="bg-slate-800 p-5 rounded-xl border border-slate-700">
          <span className="text-slate-400 text-xs uppercase font-medium">Relación Beneficio / Costo</span>
          <p className="text-2xl font-bold text-purple-400 mt-1">{data.metricas_clave.relacion_bc}x</p>
        </div>
      </section>

      {/* Ratios y Escenarios */}
      <div className="grid grid-cols-1 lg:grid-cols-2 gap-8 mb-8">
        {/* Tabla de Ratios */}
        <div className="bg-slate-800 p-6 rounded-xl border border-slate-700">
          <h2 className="text-lg font-semibold text-white mb-4">Razones Financieras Clave</h2>
          <div className="space-y-3">
            <div className="flex justify-between border-b border-slate-700 pb-2 text-sm">
              <span className="text-slate-300">ROA (Retorno s/ Activos)</span>
              <span className="font-mono text-emerald-400">{(data.razones_financieras.roa * 100).toFixed(1)}%</span>
            </div>
            <div className="flex justify-between border-b border-slate-700 pb-2 text-sm">
              <span className="text-slate-300">ROE (Retorno s/ Patrimonio)</span>
              <span className="font-mono text-emerald-400">{(data.razones_financieras.roe * 100).toFixed(1)}%</span>
            </div>
            <div className="flex justify-between border-b border-slate-700 pb-2 text-sm">
              <span className="text-slate-300">Nivel de Endeudamiento</span>
              <span className="font-mono text-amber-400">{(data.razones_financieras.endeudamiento_total * 100).toFixed(1)}%</span>
            </div>
          </div>
        </div>

        {/* Recomendación Final */}
        <div className="bg-slate-800 p-6 rounded-xl border border-slate-700 border-l-4 border-l-rose-500">
          <h2 className="text-lg font-semibold text-white mb-2">Recomendación Sustentada</h2>
          <p className="text-slate-300 text-sm leading-relaxed">{data.recomendacion}</p>
          <div className="mt-4 text-xs text-slate-500">Actualizado: {data.fecha_actualizacion}</div>
        </div>
      </div>
    </div>
  );
}
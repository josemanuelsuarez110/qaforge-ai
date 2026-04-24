import { NextResponse } from "next/server";
import { hasSupabaseConfig, supabase } from "../../../../lib/supabase.js";

export async function GET() {
  if (hasSupabaseConfig) {
    const { data, error } = await supabase
      .from("ai_suggestions")
      .select("suggestion")
      .order("created_at", { ascending: false })
      .limit(10);

    if (!error && data?.length) {
      return NextResponse.json({
        suggestions: data.map(item => item.suggestion)
      });
    }
  }

  return NextResponse.json({
    suggestions: [
      "Agrega casos de retry para autenticacion fallida en mobile.",
      "Crea un smoke test para rollback de pagos cuando falle el proveedor externo.",
      "Incluye cobertura de expiracion de sesion en escenarios de checkout."
    ]
  });
}

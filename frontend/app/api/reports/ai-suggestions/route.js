import { NextResponse } from "next/server";

export async function GET() {
  return NextResponse.json({
    suggestions: [
      "Agrega casos de retry para autenticacion fallida en mobile.",
      "Crea un smoke test para rollback de pagos cuando falle el proveedor externo.",
      "Incluye cobertura de expiracion de sesion en escenarios de checkout."
    ]
  });
}

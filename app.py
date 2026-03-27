# Lógica
if data_ferias > hoje:
    diferenca_total = data_ferias - hoje
    total_dias = diferenca_total.days

    diferenca_relativa = relativedelta(data_ferias, hoje)
    anos = diferenca_relativa.years
    meses = diferenca_relativa.months
    dias_restantes = diferenca_relativa.days

    st.subheader(
        "Do dia {} até {}:".format(
            hoje.strftime('%d/%m/%Y'),
            data_ferias.strftime('%d/%m/%Y')
        )
    )

    col1, col2 = st.columns(2)

    with col1:
        st.info(f"📅 **Total de dias:**\n\n# {total_dias} dias")

    with col2:
        partes = []

        if anos > 0:
            partes.append(f"{anos} ano" if anos == 1 else f"{anos} anos")
        if meses > 0:
            partes.append(f"{meses} mês" if meses == 1 else f"{meses} meses")
        if dias_restantes > 0:
            partes.append(f"{dias_restantes} dia" if dias_restantes == 1 else f"{dias_restantes} dias")

        if not partes:
            texto_equivalente = "0 dias"
        elif len(partes) == 1:
            texto_equivalente = partes[0]
        elif len(partes) == 2:
            texto_equivalente = " e ".join(partes)
        else:
            texto_equivalente = f"{partes[0]}, {partes[1]} e {partes[2]}"

        st.success(f"📆 **Equivalente a:**\n\n# {texto_equivalente}")

elif data_ferias == hoje:
    st.balloons()
    st.success("🎉 É hoje! Boas férias!")

else:
    st.warning("Essa data já passou!")

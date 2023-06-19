import bin


def main() -> None:
    document = ExtStat.read_pdf("SESJA_PP_PYTANIA.pdf")

    print(document)


if __name__ == "__main__":
    main()

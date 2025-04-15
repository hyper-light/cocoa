from cocoa.cli.arg_types.data_types.check_if_multiarg import check_if_multiarg


def run():
    Test = list[str] | None

    print(check_if_multiarg(Test))


run()
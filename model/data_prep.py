import sys
import time
import pandas as pd


def add_features(f_in, f_out):
    df = pd.read_csv(f_in, sep=";", header=0)
    # todo
    # phase: 'Package_Accept'
    # resource: 'ER_00251_ER_00251'
    # phase_duration: '42'
    # steps: '6'
    # process: '_Analyze-Analyze_Design-Design_Build-Build_Test-Test_Package-Package_Accept'
    # progress: [deployed, complete_but_not_deployed, started, in_analysis]
    # one_of_7_scenarios: '1'
    # weekday: 'Mon'
    # hour_of_the_day: '17'
    # active_processes: '17'
    # duration_in_working_hours: '0'
    df.to_csv(f_out, sep=";")


def main():
    f_in = sys.argv[1]
    f_out = sys.argv[2]
    start_time = time.time()
    add_features(f_in, f_out)
    print("--- done in %s seconds ---" % (time.time() - start_time))


if __name__ == "__main__":
    main()

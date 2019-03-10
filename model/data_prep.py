import datetime as dt
import sys
import time
import pandas as pd


def add_features(f_in, f_out):
    df = pd.read_csv(f_in, sep=";", header=0, dtype='str')

    # replace all empty cells with nan, so new features are created easier
    df.fillna(value="nan", inplace=True)
    df.sort_values(['work_item', 'timestamp'], ascending=[False, False], inplace=True)
    # unix timestamp
    df['time'] = df['timestamp'].apply(lambda x: time.mktime(dt.datetime.strptime(x, "%Y-%m-%d %H:%M:%S").timetuple()))
    df['phase'] = df.from_phase + "_" + df.to_phase
    df['resource'] = df.from_resource + "_" + df.to_resource
    # duration = seconds between this timestamp and the next one
    df['duration'] = "0"
    df.ix[(df.work_item == df.shift(1).work_item), 'duration'] = df.shift(1).time - df.time
    # how many steps does this process have
    df['steps'] = df.groupby('work_item')['work_item'].transform('count')

    # todo
    # process: '_Analyze-Analyze_Design-Design_Build-Build_Test-Test_Package-Package_Accept'
    # progress: [deployed, complete_but_not_deployed, started, in_analysis]
    # one_of_7_scenarios: '1'
    # weekday: 'Mon'
    # hour_of_the_day: '17'
    # active_processes: '17'
    # duration_in_working_hours: '0'

    df.to_csv(f_out, sep=";")
    df.head()


def main():
    f_in = sys.argv[1]
    f_out = sys.argv[2]
    start_time = time.time()
    add_features(f_in, f_out)
    print("--- done in %s seconds ---" % (time.time() - start_time))


if __name__ == "__main__":
    main()

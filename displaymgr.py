import datetime
import json
import icalendar
class DisplayMgr:
    def print_generation(self, population):
        schedules = population.get_schedules()
        print("fitness: " + str(schedules[0].get_fitness()))


    def get_ics_data(self, classes, cname):
        u_id = 0
        cal = icalendar.Calendar()
        cal.add('prodid', '-//Unimy Calendar//unimu.pp.ua//')
        cal.add('version', '2.0')

        next_sunday = datetime.datetime(year=2023, month=2, day=26, hour=0, minute=0, second=0)

        wd_to_index_map = {
            'sun': 0,
            'mon': 1,
            'tue': 2,
            'wed': 3,
            'thu': 4,
            'fri': 5
        }
        for j in range(10):
            for i in classes:
                start_hour = i.get_timeslot().get_timestamp()[0].hour
                start_mins = i.get_timeslot().get_timestamp()[0].minute
                end_hour = i.get_timeslot().get_timestamp()[1].hour
                end_mins = i.get_timeslot().get_timestamp()[1].minute

                start_time_datetime = next_sunday + datetime.timedelta(
                    days=wd_to_index_map[i.get_day()]) + datetime.timedelta(days=j * 7)
                start_time_datetimeS = start_time_datetime + datetime.timedelta(hours=start_hour, minutes=start_mins,
                                                                                seconds=0)
                end_time_datetimeE = start_time_datetime + datetime.timedelta(hours=end_hour, minutes=end_mins,
                                                                              seconds=0)

                event = icalendar.Event()
                event.add('summary', f"{i.get_course().get_name()}\n {i.get_instructor().get_name()}")
                event.add('dtstart', start_time_datetimeS)
                event.add('dtend', end_time_datetimeE)
                event['location'] = icalendar.vText('Pulchowk, Nepal')
                event['uid'] = u_id
                event.add('priority', 5)
                u_id += 1
                cal.add_component(event)

        f = open(f'./output/{cname}.ics', 'wb')
        f.write(cal.to_ical())
        f.close()

    def json_parser(self, classes, filename):
        next_sunday = datetime.datetime(year=2023, month=2, day=26, hour=0, minute=0, second=0)
        wd_to_index_map = {
            'sun': 0,
            'mon': 1,
            'tue': 2,
            'wed': 3,
            'thu': 4,
            'fri': 5
        }
        jsoned = {}
        dic_list = []
        for j in range(10):
            for i in classes:
                start_hour = i.get_timeslot().get_timestamp()[0].hour
                start_mins = i.get_timeslot().get_timestamp()[0].minute
                end_hour = i.get_timeslot().get_timestamp()[1].hour
                end_mins = i.get_timeslot().get_timestamp()[1].minute

                start_time_datetime = next_sunday + datetime.timedelta(
                    days=wd_to_index_map[i.get_day()]) + datetime.timedelta(days=7 * j)
                start_time_datetimeS = start_time_datetime + datetime.timedelta(hours=start_hour, minutes=start_mins,
                                                                                seconds=0)
                end_time_datetimeE = start_time_datetime + datetime.timedelta(hours=end_hour, minutes=end_mins,
                                                                              seconds=0)
                dic = {}
                dic["name"] = f"{i.get_course().get_name()} [{i.get_instructor().get_name()}]"
                dic["from"] = str(start_time_datetimeS)
                dic["to"] = str(end_time_datetimeE)
                dic_list.append(dic)
        jsoned["classes"] = dic_list

        with open(f'./output/{filename}.ics', "w") as f:
            json.dump(jsoned, f, indent=4)
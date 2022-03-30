from mycroft import MycroftSkill, intent_file_handler


class TripDetails(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('details.trip.intent')
    def handle_details_trip(self, message):
        end_trip = ''
        start_trip = ''

        self.speak_dialog('details.trip', data={
            'start_trip': start_trip,
            'end_trip': end_trip
        })


def create_skill():
    return TripDetails()


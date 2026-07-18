# === Stage 16: Добавь расчёт месячной статистики по датам ===
# Project: CourseSchedule
class MonthlyStatsCalculator:
    """Calculates monthly statistics from attendance records."""

    def __init__(self, attendance_records):
        self.records = attendance_records

    @staticmethod
    def get_monthly_attendance(attendance_records, start_date, end_date):
        """Returns a dict with month keys and total attendance values for that month.

        Args:
            attendance_records (list[AttendanceRecord]): list of records to process.
            start_date (datetime.date): first day of the reporting period.
            end_date (datetime.date): last day of the reporting period.

        Returns:
            dict[str, int]: {YYYY-MM: total_attendance_count}
        """
        stats = {}
        current = start_date.replace(day=1)
        while current <= end_date:
            month_key = current.strftime("%Y-%m")
            if month_key not in stats:
                stats[month_key] = 0
            for record in attendance_records:
                if (record.date >= current and
                        record.date < current.replace(day=1) + timedelta(days=32)):
                    stats[month_key] += record.attendance_count
            next_month = current.replace(day=1) + timedelta(days=32).replace(day=1)
            current = next_month

        return stats

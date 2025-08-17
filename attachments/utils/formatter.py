class Formatter:
    def format_byte(bytes_num):
        suffixes = ['B', 'KB', 'MB', 'GB', 'TB']
        i = 0
        while bytes_num >= 1024 and i < len(suffixes) - 1:
            bytes_num /= 1024.0
            i += 1
        return "{:.3g} {}".format(bytes_num, suffixes[i])
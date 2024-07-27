dataset["Suhu"]=0
for i in range(len(dataset)):
    match dataset["year"][i]:
        case 2021:
            match dataset["month"][i]:
                case 1:
                    print("No Data")
                case 2:
                    print("No Data")
                case 3:
                    print("No Data")
                case 4:
                    print("No Data")
                case 5:
                    print("No Data")
                case 6:
                    print("No Data")
                case 7:
                    print("No Data")
                case 8:
                    print("No Data")
                case 9:
                    dataset["Suhu"][i] = round(random.uniform(19, 35.6),1)
                    match dataset['day'][i]:
                        case 1:
                           for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2021][dataset["day"]==1][dataset["month"]==9][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 2:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2021][dataset["day"]==2][dataset["month"]==9][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 3:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2021][dataset["day"]==3][dataset["month"]==9][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 4:
                             for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2021][dataset["day"]==4][dataset["month"]==9][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 5:
                             for j in range(i):
                                if dataset['year'][j] == dataset['year'][i]:
                                        if dataset['month'][j] == dataset['month'][i]:
                                            if dataset['day'][j] == dataset['day'][i]:
                                                dataset["Suhu"][i]= dataset["Suhu"][j]
                        case 6:
                            for j in range(i):
                                if dataset['year'][j] == dataset['year'][i]:
                                        if dataset['month'][j] == dataset['month'][i]:
                                            if dataset['day'][j] == dataset['day'][i]:
                                                dataset["Suhu"][i]= dataset["Suhu"][j]
                        case 7:
                            for j in range(i):
                                if dataset['year'][j] == dataset['year'][i]:
                                        if dataset['month'][j] == dataset['month'][i]:
                                            if dataset['day'][j] == dataset['day'][i]:
                                                dataset["Suhu"][i]= dataset["Suhu"][j]
                        case 8:
                            for j in range(i):
                                if dataset['year'][j] == dataset['year'][i]:
                                        if dataset['month'][j] == dataset['month'][i]:
                                            if dataset['day'][j] == dataset['day'][i]:
                                                dataset["Suhu"][i]= dataset["Suhu"][j]
                        case 9:
                            for j in range(i):
                                if dataset['year'][j] == dataset['year'][i]:
                                        if dataset['month'][j] == dataset['month'][i]:
                                            if dataset['day'][j] == dataset['day'][i]:
                                                dataset["Suhu"][i]= dataset["Suhu"][j]
                        case 10:
                            for j in range(i):
                                if dataset['year'][j] == dataset['year'][i]:
                                        if dataset['month'][j] == dataset['month'][i]:
                                            if dataset['day'][j] == dataset['day'][i]:
                                                dataset["Suhu"][i]= dataset["Suhu"][j]
                        case 11:
                            for j in range(i):
                                if dataset['year'][j] == dataset['year'][i]:
                                        if dataset['month'][j] == dataset['month'][i]:
                                            if dataset['day'][j] == dataset['day'][i]:
                                                dataset["Suhu"][i]= dataset["Suhu"][j]
                        case 12:
                            for j in range(i):
                                if dataset['year'][j] == dataset['year'][i]:
                                        if dataset['month'][j] == dataset['month'][i]:
                                            if dataset['day'][j] == dataset['day'][i]:
                                                dataset["Suhu"][i]= dataset["Suhu"][j]
                        case 13:
                            for j in range(i):
                                if dataset['year'][j] == dataset['year'][i]:
                                        if dataset['month'][j] == dataset['month'][i]:
                                            if dataset['day'][j] == dataset['day'][i]:
                                                dataset["Suhu"][i]= dataset["Suhu"][j]
                        case 14:
                            for j in range(i):
                                if dataset['year'][j] == dataset['year'][i]:
                                        if dataset['month'][j] == dataset['month'][i]:
                                            if dataset['day'][j] == dataset['day'][i]:
                                                dataset["Suhu"][i]= dataset["Suhu"][j]
                        case 15:
                            for j in range(i):
                                if dataset['year'][j] == dataset['year'][i]:
                                        if dataset['month'][j] == dataset['month'][i]:
                                            if dataset['day'][j] == dataset['day'][i]:
                                                dataset["Suhu"][i]= dataset["Suhu"][j]
                        case 16:
                            for j in range(i):
                                if dataset['year'][j] == dataset['year'][i]:
                                        if dataset['month'][j] == dataset['month'][i]:
                                            if dataset['day'][j] == dataset['day'][i]:
                                                dataset["Suhu"][i]= dataset["Suhu"][j]
                        case 17:
                            for j in range(i):
                                if dataset['year'][j] == dataset['year'][i]:
                                        if dataset['month'][j] == dataset['month'][i]:
                                            if dataset['day'][j] == dataset['day'][i]:
                                                dataset["Suhu"][i]= dataset["Suhu"][j]
                        case 18:
                            for j in range(i):
                                if dataset['year'][j] == dataset['year'][i]:
                                        if dataset['month'][j] == dataset['month'][i]:
                                            if dataset['day'][j] == dataset['day'][i]:
                                                dataset["Suhu"][i]= dataset["Suhu"][j]
                        case 19:
                            for j in range(i):
                                if dataset['year'][j] == dataset['year'][i]:
                                        if dataset['month'][j] == dataset['month'][i]:
                                            if dataset['day'][j] == dataset['day'][i]:
                                                dataset["Suhu"][i]= dataset["Suhu"][j]
                        case 20:
                            for j in range(i):
                                if dataset['year'][j] == dataset['year'][i]:
                                        if dataset['month'][j] == dataset['month'][i]:
                                            if dataset['day'][j] == dataset['day'][i]:
                                                dataset["Suhu"][i]= dataset["Suhu"][j]
                        case 21:
                            for j in range(i):
                                if dataset['year'][j] == dataset['year'][i]:
                                        if dataset['month'][j] == dataset['month'][i]:
                                            if dataset['day'][j] == dataset['day'][i]:
                                                dataset["Suhu"][i]= dataset["Suhu"][j]
                        case 22:
                            for j in range(i):
                                if dataset['year'][j] == dataset['year'][i]:
                                        if dataset['month'][j] == dataset['month'][i]:
                                            if dataset['day'][j] == dataset['day'][i]:
                                                dataset["Suhu"][i]= dataset["Suhu"][j]
                        case 23:
                            for j in range(i):
                                if dataset['year'][j] == dataset['year'][i]:
                                        if dataset['month'][j] == dataset['month'][i]:
                                            if dataset['day'][j] == dataset['day'][i]:
                                                dataset["Suhu"][i]= dataset["Suhu"][j]
                        case 24:
                            for j in range(i):
                                if dataset['year'][j] == dataset['year'][i]:
                                        if dataset['month'][j] == dataset['month'][i]:
                                            if dataset['day'][j] == dataset['day'][i]:
                                                dataset["Suhu"][i]= dataset["Suhu"][j]
                        case 25:
                            for j in range(i):
                                if dataset['year'][j] == dataset['year'][i]:
                                        if dataset['month'][j] == dataset['month'][i]:
                                            if dataset['day'][j] == dataset['day'][i]:
                                                dataset["Suhu"][i]= dataset["Suhu"][j]
                        case 26:
                            for j in range(i):
                                if dataset['year'][j] == dataset['year'][i]:
                                        if dataset['month'][j] == dataset['month'][i]:
                                            if dataset['day'][j] == dataset['day'][i]:
                                                dataset["Suhu"][i]= dataset["Suhu"][j]
                        case 27:
                            for j in range(i):
                                if dataset['year'][j] == dataset['year'][i]:
                                        if dataset['month'][j] == dataset['month'][i]:
                                            if dataset['day'][j] == dataset['day'][i]:
                                                dataset["Suhu"][i]= dataset["Suhu"][j]
                        case 28:
                            for j in range(i):
                                if dataset['year'][j] == dataset['year'][i]:
                                        if dataset['month'][j] == dataset['month'][i]:
                                            if dataset['day'][j] == dataset['day'][i]:
                                                dataset["Suhu"][i]= dataset["Suhu"][j]
                        case 29:
                            for j in range(i):
                                if dataset['year'][j] == dataset['year'][i]:
                                        if dataset['month'][j] == dataset['month'][i]:
                                            if dataset['day'][j] == dataset['day'][i]:
                                                dataset["Suhu"][i]= dataset["Suhu"][j]
                        case 30:
                            for j in range(i):
                                if dataset['year'][j] == dataset['year'][i]:
                                        if dataset['month'][j] == dataset['month'][i]:
                                            if dataset['day'][j] == dataset['day'][i]:
                                                dataset["Suhu"][i]= dataset["Suhu"][j]
                        case 31:
                            for j in range(i):
                                if dataset['year'][j] == dataset['year'][i]:
                                        if dataset['month'][j] == dataset['month'][i]:
                                            if dataset['day'][j] == dataset['day'][i]:
                                                dataset["Suhu"][i]= dataset["Suhu"][j]
                case 10:
                    dataset["Suhu"][i] = round(random.uniform(19, 35.6),1)
                    match dataset['day'][i]:
                        case 1:
                           for j in range(i):
                                if dataset['year'][j] == dataset['year'][i]:
                                        if dataset['month'][j] == dataset['month'][i]:
                                            if dataset['day'][j] == dataset['day'][i]:
                                                dataset["Suhu"][i]= dataset["Suhu"][j]
                        case 2:
                            for j in range(i):
                                if dataset['year'][j] == dataset['year'][i]:
                                        if dataset['month'][j] == dataset['month'][i]:
                                            if dataset['day'][j] == dataset['day'][i]:
                                                dataset["Suhu"][i]= dataset["Suhu"][j]
                        case 3:
                            for j in range(i):
                                if dataset['year'][j] == dataset['year'][i]:
                                        if dataset['month'][j] == dataset['month'][i]:
                                            if dataset['day'][j] == dataset['day'][i]:
                                                dataset["Suhu"][i]= dataset["Suhu"][j]
                        case 4:
                             for j in range(i):
                                if dataset['year'][j] == dataset['year'][i]:
                                        if dataset['month'][j] == dataset['month'][i]:
                                            if dataset['day'][j] == dataset['day'][i]:
                                                dataset["Suhu"][i]= dataset["Suhu"][j]
                        case 5:
                             for j in range(i):
                                if dataset['year'][j] == dataset['year'][i]:
                                        if dataset['month'][j] == dataset['month'][i]:
                                            if dataset['day'][j] == dataset['day'][i]:
                                                dataset["Suhu"][i]= dataset["Suhu"][j]
                        case 6:
                            for j in range(i):
                                if dataset['year'][j] == dataset['year'][i]:
                                        if dataset['month'][j] == dataset['month'][i]:
                                            if dataset['day'][j] == dataset['day'][i]:
                                                dataset["Suhu"][i]= dataset["Suhu"][j]
                        case 7:
                            for j in range(i):
                                if dataset['year'][j] == dataset['year'][i]:
                                        if dataset['month'][j] == dataset['month'][i]:
                                            if dataset['day'][j] == dataset['day'][i]:
                                                dataset["Suhu"][i]= dataset["Suhu"][j]
                        case 8:
                            for j in range(i):
                                if dataset['year'][j] == dataset['year'][i]:
                                        if dataset['month'][j] == dataset['month'][i]:
                                            if dataset['day'][j] == dataset['day'][i]:
                                                dataset["Suhu"][i]= dataset["Suhu"][j]
                        case 9:
                            for j in range(i):
                                if dataset['year'][j] == dataset['year'][i]:
                                        if dataset['month'][j] == dataset['month'][i]:
                                            if dataset['day'][j] == dataset['day'][i]:
                                                dataset["Suhu"][i]= dataset["Suhu"][j]
                        case 10:
                            for j in range(i):
                                if dataset['year'][j] == dataset['year'][i]:
                                        if dataset['month'][j] == dataset['month'][i]:
                                            if dataset['day'][j] == dataset['day'][i]:
                                                dataset["Suhu"][i]= dataset["Suhu"][j]
                        case 11:
                            for j in range(i):
                                if dataset['year'][j] == dataset['year'][i]:
                                        if dataset['month'][j] == dataset['month'][i]:
                                            if dataset['day'][j] == dataset['day'][i]:
                                                dataset["Suhu"][i]= dataset["Suhu"][j]
                        case 12:
                            for j in range(i):
                                if dataset['year'][j] == dataset['year'][i]:
                                        if dataset['month'][j] == dataset['month'][i]:
                                            if dataset['day'][j] == dataset['day'][i]:
                                                dataset["Suhu"][i]= dataset["Suhu"][j]
                        case 13:
                            for j in range(i):
                                if dataset['year'][j] == dataset['year'][i]:
                                        if dataset['month'][j] == dataset['month'][i]:
                                            if dataset['day'][j] == dataset['day'][i]:
                                                dataset["Suhu"][i]= dataset["Suhu"][j]
                        case 14:
                            for j in range(i):
                                if dataset['year'][j] == dataset['year'][i]:
                                        if dataset['month'][j] == dataset['month'][i]:
                                            if dataset['day'][j] == dataset['day'][i]:
                                                dataset["Suhu"][i]= dataset["Suhu"][j]
                        case 15:
                            for j in range(i):
                                if dataset['year'][j] == dataset['year'][i]:
                                        if dataset['month'][j] == dataset['month'][i]:
                                            if dataset['day'][j] == dataset['day'][i]:
                                                dataset["Suhu"][i]= dataset["Suhu"][j]
                        case 16:
                            for j in range(i):
                                if dataset['year'][j] == dataset['year'][i]:
                                        if dataset['month'][j] == dataset['month'][i]:
                                            if dataset['day'][j] == dataset['day'][i]:
                                                dataset["Suhu"][i]= dataset["Suhu"][j]
                        case 17:
                            for j in range(i):
                                if dataset['year'][j] == dataset['year'][i]:
                                        if dataset['month'][j] == dataset['month'][i]:
                                            if dataset['day'][j] == dataset['day'][i]:
                                                dataset["Suhu"][i]= dataset["Suhu"][j]
                        case 18:
                            for j in range(i):
                                if dataset['year'][j] == dataset['year'][i]:
                                        if dataset['month'][j] == dataset['month'][i]:
                                            if dataset['day'][j] == dataset['day'][i]:
                                                dataset["Suhu"][i]= dataset["Suhu"][j]
                        case 19:
                            for j in range(i):
                                if dataset['year'][j] == dataset['year'][i]:
                                        if dataset['month'][j] == dataset['month'][i]:
                                            if dataset['day'][j] == dataset['day'][i]:
                                                dataset["Suhu"][i]= dataset["Suhu"][j]
                        case 20:
                            for j in range(i):
                                if dataset['year'][j] == dataset['year'][i]:
                                        if dataset['month'][j] == dataset['month'][i]:
                                            if dataset['day'][j] == dataset['day'][i]:
                                                dataset["Suhu"][i]= dataset["Suhu"][j]
                        case 21:
                            for j in range(i):
                                if dataset['year'][j] == dataset['year'][i]:
                                        if dataset['month'][j] == dataset['month'][i]:
                                            if dataset['day'][j] == dataset['day'][i]:
                                                dataset["Suhu"][i]= dataset["Suhu"][j]
                        case 22:
                            for j in range(i):
                                if dataset['year'][j] == dataset['year'][i]:
                                        if dataset['month'][j] == dataset['month'][i]:
                                            if dataset['day'][j] == dataset['day'][i]:
                                                dataset["Suhu"][i]= dataset["Suhu"][j]
                        case 23:
                            for j in range(i):
                                if dataset['year'][j] == dataset['year'][i]:
                                        if dataset['month'][j] == dataset['month'][i]:
                                            if dataset['day'][j] == dataset['day'][i]:
                                                dataset["Suhu"][i]= dataset["Suhu"][j]
                        case 24:
                            for j in range(i):
                                if dataset['year'][j] == dataset['year'][i]:
                                        if dataset['month'][j] == dataset['month'][i]:
                                            if dataset['day'][j] == dataset['day'][i]:
                                                dataset["Suhu"][i]= dataset["Suhu"][j]
                        case 25:
                            for j in range(i):
                                if dataset['year'][j] == dataset['year'][i]:
                                        if dataset['month'][j] == dataset['month'][i]:
                                            if dataset['day'][j] == dataset['day'][i]:
                                                dataset["Suhu"][i]= dataset["Suhu"][j]
                        case 26:
                            for j in range(i):
                                if dataset['year'][j] == dataset['year'][i]:
                                        if dataset['month'][j] == dataset['month'][i]:
                                            if dataset['day'][j] == dataset['day'][i]:
                                                dataset["Suhu"][i]= dataset["Suhu"][j]
                        case 27:
                            for j in range(i):
                                if dataset['year'][j] == dataset['year'][i]:
                                        if dataset['month'][j] == dataset['month'][i]:
                                            if dataset['day'][j] == dataset['day'][i]:
                                                dataset["Suhu"][i]= dataset["Suhu"][j]
                        case 28:
                            for j in range(i):
                                if dataset['year'][j] == dataset['year'][i]:
                                        if dataset['month'][j] == dataset['month'][i]:
                                            if dataset['day'][j] == dataset['day'][i]:
                                                dataset["Suhu"][i]= dataset["Suhu"][j]
                        case 29:
                            for j in range(i):
                                if dataset['year'][j] == dataset['year'][i]:
                                        if dataset['month'][j] == dataset['month'][i]:
                                            if dataset['day'][j] == dataset['day'][i]:
                                                dataset["Suhu"][i]= dataset["Suhu"][j]
                        case 30:
                            for j in range(i):
                                if dataset['year'][j] == dataset['year'][i]:
                                        if dataset['month'][j] == dataset['month'][i]:
                                            if dataset['day'][j] == dataset['day'][i]:
                                                dataset["Suhu"][i]= dataset["Suhu"][j]
                        case 31:
                            for j in range(i):
                                if dataset['year'][j] == dataset['year'][i]:
                                        if dataset['month'][j] == dataset['month'][i]:
                                            if dataset['day'][j] == dataset['day'][i]:
                                                dataset["Suhu"][i]= dataset["Suhu"][j]
                case 11:
                    dataset["Suhu"][i] = round(random.uniform(19, 35.6),1)
                    match dataset['day'][i]:
                        case 1:
                           for j in range(i):
                                if dataset['year'][j] == dataset['year'][i]:
                                        if dataset['month'][j] == dataset['month'][i]:
                                            if dataset['day'][j] == dataset['day'][i]:
                                                dataset["Suhu"][i]= dataset["Suhu"][j]
                        case 2:
                            for j in range(i):
                                if dataset['year'][j] == dataset['year'][i]:
                                        if dataset['month'][j] == dataset['month'][i]:
                                            if dataset['day'][j] == dataset['day'][i]:
                                                dataset["Suhu"][i]= dataset["Suhu"][j]
                        case 3:
                            for j in range(i):
                                if dataset['year'][j] == dataset['year'][i]:
                                        if dataset['month'][j] == dataset['month'][i]:
                                            if dataset['day'][j] == dataset['day'][i]:
                                                dataset["Suhu"][i]= dataset["Suhu"][j]
                        case 4:
                             for j in range(i):
                                if dataset['year'][j] == dataset['year'][i]:
                                        if dataset['month'][j] == dataset['month'][i]:
                                            if dataset['day'][j] == dataset['day'][i]:
                                                dataset["Suhu"][i]= dataset["Suhu"][j]
                        case 5:
                             for j in range(i):
                                if dataset['year'][j] == dataset['year'][i]:
                                        if dataset['month'][j] == dataset['month'][i]:
                                            if dataset['day'][j] == dataset['day'][i]:
                                                dataset["Suhu"][i]= dataset["Suhu"][j]
                        case 6:
                            for j in range(i):
                                if dataset['year'][j] == dataset['year'][i]:
                                        if dataset['month'][j] == dataset['month'][i]:
                                            if dataset['day'][j] == dataset['day'][i]:
                                                dataset["Suhu"][i]= dataset["Suhu"][j]
                        case 7:
                            for j in range(i):
                                if dataset['year'][j] == dataset['year'][i]:
                                        if dataset['month'][j] == dataset['month'][i]:
                                            if dataset['day'][j] == dataset['day'][i]:
                                                dataset["Suhu"][i]= dataset["Suhu"][j]
                        case 8:
                            for j in range(i):
                                if dataset['year'][j] == dataset['year'][i]:
                                        if dataset['month'][j] == dataset['month'][i]:
                                            if dataset['day'][j] == dataset['day'][i]:
                                                dataset["Suhu"][i]= dataset["Suhu"][j]
                        case 9:
                            for j in range(i):
                                if dataset['year'][j] == dataset['year'][i]:
                                        if dataset['month'][j] == dataset['month'][i]:
                                            if dataset['day'][j] == dataset['day'][i]:
                                                dataset["Suhu"][i]= dataset["Suhu"][j]
                        case 10:
                            for j in range(i):
                                if dataset['year'][j] == dataset['year'][i]:
                                        if dataset['month'][j] == dataset['month'][i]:
                                            if dataset['day'][j] == dataset['day'][i]:
                                                dataset["Suhu"][i]= dataset["Suhu"][j]
                        case 11:
                            for j in range(i):
                                if dataset['year'][j] == dataset['year'][i]:
                                        if dataset['month'][j] == dataset['month'][i]:
                                            if dataset['day'][j] == dataset['day'][i]:
                                                dataset["Suhu"][i]= dataset["Suhu"][j]
                        case 12:
                            for j in range(i):
                                if dataset['year'][j] == dataset['year'][i]:
                                        if dataset['month'][j] == dataset['month'][i]:
                                            if dataset['day'][j] == dataset['day'][i]:
                                                dataset["Suhu"][i]= dataset["Suhu"][j]
                        case 13:
                            for j in range(i):
                                if dataset['year'][j] == dataset['year'][i]:
                                        if dataset['month'][j] == dataset['month'][i]:
                                            if dataset['day'][j] == dataset['day'][i]:
                                                dataset["Suhu"][i]= dataset["Suhu"][j]
                        case 14:
                            for j in range(i):
                                if dataset['year'][j] == dataset['year'][i]:
                                        if dataset['month'][j] == dataset['month'][i]:
                                            if dataset['day'][j] == dataset['day'][i]:
                                                dataset["Suhu"][i]= dataset["Suhu"][j]
                        case 15:
                            for j in range(i):
                                if dataset['year'][j] == dataset['year'][i]:
                                        if dataset['month'][j] == dataset['month'][i]:
                                            if dataset['day'][j] == dataset['day'][i]:
                                                dataset["Suhu"][i]= dataset["Suhu"][j]
                        case 16:
                            for j in range(i):
                                if dataset['year'][j] == dataset['year'][i]:
                                        if dataset['month'][j] == dataset['month'][i]:
                                            if dataset['day'][j] == dataset['day'][i]:
                                                dataset["Suhu"][i]= dataset["Suhu"][j]
                        case 17:
                            for j in range(i):
                                if dataset['year'][j] == dataset['year'][i]:
                                        if dataset['month'][j] == dataset['month'][i]:
                                            if dataset['day'][j] == dataset['day'][i]:
                                                dataset["Suhu"][i]= dataset["Suhu"][j]
                        case 18:
                            for j in range(i):
                                if dataset['year'][j] == dataset['year'][i]:
                                        if dataset['month'][j] == dataset['month'][i]:
                                            if dataset['day'][j] == dataset['day'][i]:
                                                dataset["Suhu"][i]= dataset["Suhu"][j]
                        case 19:
                            for j in range(i):
                                if dataset['year'][j] == dataset['year'][i]:
                                        if dataset['month'][j] == dataset['month'][i]:
                                            if dataset['day'][j] == dataset['day'][i]:
                                                dataset["Suhu"][i]= dataset["Suhu"][j]
                        case 20:
                            for j in range(i):
                                if dataset['year'][j] == dataset['year'][i]:
                                        if dataset['month'][j] == dataset['month'][i]:
                                            if dataset['day'][j] == dataset['day'][i]:
                                                dataset["Suhu"][i]= dataset["Suhu"][j]
                        case 21:
                            for j in range(i):
                                if dataset['year'][j] == dataset['year'][i]:
                                        if dataset['month'][j] == dataset['month'][i]:
                                            if dataset['day'][j] == dataset['day'][i]:
                                                dataset["Suhu"][i]= dataset["Suhu"][j]
                        case 22:
                            for j in range(i):
                                if dataset['year'][j] == dataset['year'][i]:
                                        if dataset['month'][j] == dataset['month'][i]:
                                            if dataset['day'][j] == dataset['day'][i]:
                                                dataset["Suhu"][i]= dataset["Suhu"][j]
                        case 23:
                            for j in range(i):
                                if dataset['year'][j] == dataset['year'][i]:
                                        if dataset['month'][j] == dataset['month'][i]:
                                            if dataset['day'][j] == dataset['day'][i]:
                                                dataset["Suhu"][i]= dataset["Suhu"][j]
                        case 24:
                            for j in range(i):
                                if dataset['year'][j] == dataset['year'][i]:
                                        if dataset['month'][j] == dataset['month'][i]:
                                            if dataset['day'][j] == dataset['day'][i]:
                                                dataset["Suhu"][i]= dataset["Suhu"][j]
                        case 25:
                            for j in range(i):
                                if dataset['year'][j] == dataset['year'][i]:
                                        if dataset['month'][j] == dataset['month'][i]:
                                            if dataset['day'][j] == dataset['day'][i]:
                                                dataset["Suhu"][i]= dataset["Suhu"][j]
                        case 26:
                            for j in range(i):
                                if dataset['year'][j] == dataset['year'][i]:
                                        if dataset['month'][j] == dataset['month'][i]:
                                            if dataset['day'][j] == dataset['day'][i]:
                                                dataset["Suhu"][i]= dataset["Suhu"][j]
                        case 27:
                            for j in range(i):
                                if dataset['year'][j] == dataset['year'][i]:
                                        if dataset['month'][j] == dataset['month'][i]:
                                            if dataset['day'][j] == dataset['day'][i]:
                                                dataset["Suhu"][i]= dataset["Suhu"][j]
                        case 28:
                            for j in range(i):
                                if dataset['year'][j] == dataset['year'][i]:
                                        if dataset['month'][j] == dataset['month'][i]:
                                            if dataset['day'][j] == dataset['day'][i]:
                                                dataset["Suhu"][i]= dataset["Suhu"][j]
                        case 29:
                            for j in range(i):
                                if dataset['year'][j] == dataset['year'][i]:
                                        if dataset['month'][j] == dataset['month'][i]:
                                            if dataset['day'][j] == dataset['day'][i]:
                                                dataset["Suhu"][i]= dataset["Suhu"][j]
                        case 30:
                            for j in range(i):
                                if dataset['year'][j] == dataset['year'][i]:
                                        if dataset['month'][j] == dataset['month'][i]:
                                            if dataset['day'][j] == dataset['day'][i]:
                                                dataset["Suhu"][i]= dataset["Suhu"][j]
                        case 31:
                            for j in range(i):
                                if dataset['year'][j] == dataset['year'][i]:
                                        if dataset['month'][j] == dataset['month'][i]:
                                            if dataset['day'][j] == dataset['day'][i]:
                                                dataset["Suhu"][i]= dataset["Suhu"][j]
                case 12:
                    dataset["Suhu"][i] = round(random.uniform(19, 35.6),1)
                    match dataset['day'][i]:
                        case 1:
                           for j in range(i):
                                if dataset['year'][j] == dataset['year'][i]:
                                        if dataset['month'][j] == dataset['month'][i]:
                                            if dataset['day'][j] == dataset['day'][i]:
                                                dataset["Suhu"][i]= dataset["Suhu"][j]
                        case 2:
                            for j in range(i):
                                if dataset['year'][j] == dataset['year'][i]:
                                        if dataset['month'][j] == dataset['month'][i]:
                                            if dataset['day'][j] == dataset['day'][i]:
                                                dataset["Suhu"][i]= dataset["Suhu"][j]
                        case 3:
                            for j in range(i):
                                if dataset['year'][j] == dataset['year'][i]:
                                        if dataset['month'][j] == dataset['month'][i]:
                                            if dataset['day'][j] == dataset['day'][i]:
                                                dataset["Suhu"][i]= dataset["Suhu"][j]
                        case 4:
                             for j in range(i):
                                if dataset['year'][j] == dataset['year'][i]:
                                        if dataset['month'][j] == dataset['month'][i]:
                                            if dataset['day'][j] == dataset['day'][i]:
                                                dataset["Suhu"][i]= dataset["Suhu"][j]
                        case 5:
                             for j in range(i):
                                if dataset['year'][j] == dataset['year'][i]:
                                        if dataset['month'][j] == dataset['month'][i]:
                                            if dataset['day'][j] == dataset['day'][i]:
                                                dataset["Suhu"][i]= dataset["Suhu"][j]
                        case 6:
                            for j in range(i):
                                if dataset['year'][j] == dataset['year'][i]:
                                        if dataset['month'][j] == dataset['month'][i]:
                                            if dataset['day'][j] == dataset['day'][i]:
                                                dataset["Suhu"][i]= dataset["Suhu"][j]
                        case 7:
                            for j in range(i):
                                if dataset['year'][j] == dataset['year'][i]:
                                        if dataset['month'][j] == dataset['month'][i]:
                                            if dataset['day'][j] == dataset['day'][i]:
                                                dataset["Suhu"][i]= dataset["Suhu"][j]
                        case 8:
                            for j in range(i):
                                if dataset['year'][j] == dataset['year'][i]:
                                        if dataset['month'][j] == dataset['month'][i]:
                                            if dataset['day'][j] == dataset['day'][i]:
                                                dataset["Suhu"][i]= dataset["Suhu"][j]
                        case 9:
                            for j in range(i):
                                if dataset['year'][j] == dataset['year'][i]:
                                        if dataset['month'][j] == dataset['month'][i]:
                                            if dataset['day'][j] == dataset['day'][i]:
                                                dataset["Suhu"][i]= dataset["Suhu"][j]
                        case 10:
                            for j in range(i):
                                if dataset['year'][j] == dataset['year'][i]:
                                        if dataset['month'][j] == dataset['month'][i]:
                                            if dataset['day'][j] == dataset['day'][i]:
                                                dataset["Suhu"][i]= dataset["Suhu"][j]
                        case 11:
                            for j in range(i):
                                if dataset['year'][j] == dataset['year'][i]:
                                        if dataset['month'][j] == dataset['month'][i]:
                                            if dataset['day'][j] == dataset['day'][i]:
                                                dataset["Suhu"][i]= dataset["Suhu"][j]
                        case 12:
                            for j in range(i):
                                if dataset['year'][j] == dataset['year'][i]:
                                        if dataset['month'][j] == dataset['month'][i]:
                                            if dataset['day'][j] == dataset['day'][i]:
                                                dataset["Suhu"][i]= dataset["Suhu"][j]
                        case 13:
                            for j in range(i):
                                if dataset['year'][j] == dataset['year'][i]:
                                        if dataset['month'][j] == dataset['month'][i]:
                                            if dataset['day'][j] == dataset['day'][i]:
                                                dataset["Suhu"][i]= dataset["Suhu"][j]
                        case 14:
                            for j in range(i):
                                if dataset['year'][j] == dataset['year'][i]:
                                        if dataset['month'][j] == dataset['month'][i]:
                                            if dataset['day'][j] == dataset['day'][i]:
                                                dataset["Suhu"][i]= dataset["Suhu"][j]
                        case 15:
                            for j in range(i):
                                if dataset['year'][j] == dataset['year'][i]:
                                        if dataset['month'][j] == dataset['month'][i]:
                                            if dataset['day'][j] == dataset['day'][i]:
                                                dataset["Suhu"][i]= dataset["Suhu"][j]
                        case 16:
                            for j in range(i):
                                if dataset['year'][j] == dataset['year'][i]:
                                        if dataset['month'][j] == dataset['month'][i]:
                                            if dataset['day'][j] == dataset['day'][i]:
                                                dataset["Suhu"][i]= dataset["Suhu"][j]
                        case 17:
                            for j in range(i):
                                if dataset['year'][j] == dataset['year'][i]:
                                        if dataset['month'][j] == dataset['month'][i]:
                                            if dataset['day'][j] == dataset['day'][i]:
                                                dataset["Suhu"][i]= dataset["Suhu"][j]
                        case 18:
                            for j in range(i):
                                if dataset['year'][j] == dataset['year'][i]:
                                        if dataset['month'][j] == dataset['month'][i]:
                                            if dataset['day'][j] == dataset['day'][i]:
                                                dataset["Suhu"][i]= dataset["Suhu"][j]
                        case 19:
                            for j in range(i):
                                if dataset['year'][j] == dataset['year'][i]:
                                        if dataset['month'][j] == dataset['month'][i]:
                                            if dataset['day'][j] == dataset['day'][i]:
                                                dataset["Suhu"][i]= dataset["Suhu"][j]
                        case 20:
                            for j in range(i):
                                if dataset['year'][j] == dataset['year'][i]:
                                        if dataset['month'][j] == dataset['month'][i]:
                                            if dataset['day'][j] == dataset['day'][i]:
                                                dataset["Suhu"][i]= dataset["Suhu"][j]
                        case 21:
                            for j in range(i):
                                if dataset['year'][j] == dataset['year'][i]:
                                        if dataset['month'][j] == dataset['month'][i]:
                                            if dataset['day'][j] == dataset['day'][i]:
                                                dataset["Suhu"][i]= dataset["Suhu"][j]
                        case 22:
                            for j in range(i):
                                if dataset['year'][j] == dataset['year'][i]:
                                        if dataset['month'][j] == dataset['month'][i]:
                                            if dataset['day'][j] == dataset['day'][i]:
                                                dataset["Suhu"][i]= dataset["Suhu"][j]
                        case 23:
                            for j in range(i):
                                if dataset['year'][j] == dataset['year'][i]:
                                        if dataset['month'][j] == dataset['month'][i]:
                                            if dataset['day'][j] == dataset['day'][i]:
                                                dataset["Suhu"][i]= dataset["Suhu"][j]
                        case 24:
                            for j in range(i):
                                if dataset['year'][j] == dataset['year'][i]:
                                        if dataset['month'][j] == dataset['month'][i]:
                                            if dataset['day'][j] == dataset['day'][i]:
                                                dataset["Suhu"][i]= dataset["Suhu"][j]
                        case 25:
                            for j in range(i):
                                if dataset['year'][j] == dataset['year'][i]:
                                        if dataset['month'][j] == dataset['month'][i]:
                                            if dataset['day'][j] == dataset['day'][i]:
                                                dataset["Suhu"][i]= dataset["Suhu"][j]
                        case 26:
                            for j in range(i):
                                if dataset['year'][j] == dataset['year'][i]:
                                        if dataset['month'][j] == dataset['month'][i]:
                                            if dataset['day'][j] == dataset['day'][i]:
                                                dataset["Suhu"][i]= dataset["Suhu"][j]
                        case 27:
                            for j in range(i):
                                if dataset['year'][j] == dataset['year'][i]:
                                        if dataset['month'][j] == dataset['month'][i]:
                                            if dataset['day'][j] == dataset['day'][i]:
                                                dataset["Suhu"][i]= dataset["Suhu"][j]
                        case 28:
                            for j in range(i):
                                if dataset['year'][j] == dataset['year'][i]:
                                        if dataset['month'][j] == dataset['month'][i]:
                                            if dataset['day'][j] == dataset['day'][i]:
                                                dataset["Suhu"][i]= dataset["Suhu"][j]
                        case 29:
                            for j in range(i):
                                if dataset['year'][j] == dataset['year'][i]:
                                        if dataset['month'][j] == dataset['month'][i]:
                                            if dataset['day'][j] == dataset['day'][i]:
                                                dataset["Suhu"][i]= dataset["Suhu"][j]
                        case 30:
                            for j in range(i):
                                if dataset['year'][j] == dataset['year'][i]:
                                        if dataset['month'][j] == dataset['month'][i]:
                                            if dataset['day'][j] == dataset['day'][i]:
                                                dataset["Suhu"][i]= dataset["Suhu"][j]
                        case 31:
                            for j in range(i):
                                if dataset['year'][j] == dataset['year'][i]:
                                        if dataset['month'][j] == dataset['month'][i]:
                                            if dataset['day'][j] == dataset['day'][i]:
                                                dataset["Suhu"][i]= dataset["Suhu"][j]
        case 2022:
            match dataset["month"][i]:
                case 1:
                    dataset["Suhu"][i] = round(random.uniform(23.5, 32.6),1)
                    match dataset['day'][i]:
                        case 1:
                           for j in range(i):
                                if dataset['year'][j] == dataset['year'][i]:
                                        if dataset['month'][j] == dataset['month'][i]:
                                            if dataset['day'][j] == dataset['day'][i]:
                                                dataset["Suhu"][i]= dataset["Suhu"][j]
                        case 2:
                            for j in range(i):
                                if dataset['year'][j] == dataset['year'][i]:
                                        if dataset['month'][j] == dataset['month'][i]:
                                            if dataset['day'][j] == dataset['day'][i]:
                                                dataset["Suhu"][i]= dataset["Suhu"][j]
                        case 3:
                            for j in range(i):
                                if dataset['year'][j] == dataset['year'][i]:
                                        if dataset['month'][j] == dataset['month'][i]:
                                            if dataset['day'][j] == dataset['day'][i]:
                                                dataset["Suhu"][i]= dataset["Suhu"][j]
                        case 4:
                             for j in range(i):
                                if dataset['year'][j] == dataset['year'][i]:
                                        if dataset['month'][j] == dataset['month'][i]:
                                            if dataset['day'][j] == dataset['day'][i]:
                                                dataset["Suhu"][i]= dataset["Suhu"][j]
                        case 5:
                             for j in range(i):
                                if dataset['year'][j] == dataset['year'][i]:
                                        if dataset['month'][j] == dataset['month'][i]:
                                            if dataset['day'][j] == dataset['day'][i]:
                                                dataset["Suhu"][i]= dataset["Suhu"][j]
                        case 6:
                            for j in range(i):
                                if dataset['year'][j] == dataset['year'][i]:
                                        if dataset['month'][j] == dataset['month'][i]:
                                            if dataset['day'][j] == dataset['day'][i]:
                                                dataset["Suhu"][i]= dataset["Suhu"][j]
                        case 7:
                            for j in range(i):
                                if dataset['year'][j] == dataset['year'][i]:
                                        if dataset['month'][j] == dataset['month'][i]:
                                            if dataset['day'][j] == dataset['day'][i]:
                                                dataset["Suhu"][i]= dataset["Suhu"][j]
                        case 8:
                            for j in range(i):
                                if dataset['year'][j] == dataset['year'][i]:
                                        if dataset['month'][j] == dataset['month'][i]:
                                            if dataset['day'][j] == dataset['day'][i]:
                                                dataset["Suhu"][i]= dataset["Suhu"][j]
                        case 9:
                            for j in range(i):
                                if dataset['year'][j] == dataset['year'][i]:
                                        if dataset['month'][j] == dataset['month'][i]:
                                            if dataset['day'][j] == dataset['day'][i]:
                                                dataset["Suhu"][i]= dataset["Suhu"][j]
                        case 10:
                            for j in range(i):
                                if dataset['year'][j] == dataset['year'][i]:
                                        if dataset['month'][j] == dataset['month'][i]:
                                            if dataset['day'][j] == dataset['day'][i]:
                                                dataset["Suhu"][i]= dataset["Suhu"][j]
                        case 11:
                            for j in range(i):
                                if dataset['year'][j] == dataset['year'][i]:
                                        if dataset['month'][j] == dataset['month'][i]:
                                            if dataset['day'][j] == dataset['day'][i]:
                                                dataset["Suhu"][i]= dataset["Suhu"][j]
                        case 12:
                            for j in range(i):
                                if dataset['year'][j] == dataset['year'][i]:
                                        if dataset['month'][j] == dataset['month'][i]:
                                            if dataset['day'][j] == dataset['day'][i]:
                                                dataset["Suhu"][i]= dataset["Suhu"][j]
                        case 13:
                            for j in range(i):
                                if dataset['year'][j] == dataset['year'][i]:
                                        if dataset['month'][j] == dataset['month'][i]:
                                            if dataset['day'][j] == dataset['day'][i]:
                                                dataset["Suhu"][i]= dataset["Suhu"][j]
                        case 14:
                            for j in range(i):
                                if dataset['year'][j] == dataset['year'][i]:
                                        if dataset['month'][j] == dataset['month'][i]:
                                            if dataset['day'][j] == dataset['day'][i]:
                                                dataset["Suhu"][i]= dataset["Suhu"][j]
                        case 15:
                            for j in range(i):
                                if dataset['year'][j] == dataset['year'][i]:
                                        if dataset['month'][j] == dataset['month'][i]:
                                            if dataset['day'][j] == dataset['day'][i]:
                                                dataset["Suhu"][i]= dataset["Suhu"][j]
                        case 16:
                            for j in range(i):
                                if dataset['year'][j] == dataset['year'][i]:
                                        if dataset['month'][j] == dataset['month'][i]:
                                            if dataset['day'][j] == dataset['day'][i]:
                                                dataset["Suhu"][i]= dataset["Suhu"][j]
                        case 17:
                            for j in range(i):
                                if dataset['year'][j] == dataset['year'][i]:
                                        if dataset['month'][j] == dataset['month'][i]:
                                            if dataset['day'][j] == dataset['day'][i]:
                                                dataset["Suhu"][i]= dataset["Suhu"][j]
                        case 18:
                            for j in range(i):
                                if dataset['year'][j] == dataset['year'][i]:
                                        if dataset['month'][j] == dataset['month'][i]:
                                            if dataset['day'][j] == dataset['day'][i]:
                                                dataset["Suhu"][i]= dataset["Suhu"][j]
                        case 19:
                            for j in range(i):
                                if dataset['year'][j] == dataset['year'][i]:
                                        if dataset['month'][j] == dataset['month'][i]:
                                            if dataset['day'][j] == dataset['day'][i]:
                                                dataset["Suhu"][i]= dataset["Suhu"][j]
                        case 20:
                            for j in range(i):
                                if dataset['year'][j] == dataset['year'][i]:
                                        if dataset['month'][j] == dataset['month'][i]:
                                            if dataset['day'][j] == dataset['day'][i]:
                                                dataset["Suhu"][i]= dataset["Suhu"][j]
                        case 21:
                            for j in range(i):
                                if dataset['year'][j] == dataset['year'][i]:
                                        if dataset['month'][j] == dataset['month'][i]:
                                            if dataset['day'][j] == dataset['day'][i]:
                                                dataset["Suhu"][i]= dataset["Suhu"][j]
                        case 22:
                            for j in range(i):
                                if dataset['year'][j] == dataset['year'][i]:
                                        if dataset['month'][j] == dataset['month'][i]:
                                            if dataset['day'][j] == dataset['day'][i]:
                                                dataset["Suhu"][i]= dataset["Suhu"][j]
                        case 23:
                            for j in range(i):
                                if dataset['year'][j] == dataset['year'][i]:
                                        if dataset['month'][j] == dataset['month'][i]:
                                            if dataset['day'][j] == dataset['day'][i]:
                                                dataset["Suhu"][i]= dataset["Suhu"][j]
                        case 24:
                            for j in range(i):
                                if dataset['year'][j] == dataset['year'][i]:
                                        if dataset['month'][j] == dataset['month'][i]:
                                            if dataset['day'][j] == dataset['day'][i]:
                                                dataset["Suhu"][i]= dataset["Suhu"][j]
                        case 25:
                            for j in range(i):
                                if dataset['year'][j] == dataset['year'][i]:
                                        if dataset['month'][j] == dataset['month'][i]:
                                            if dataset['day'][j] == dataset['day'][i]:
                                                dataset["Suhu"][i]= dataset["Suhu"][j]
                        case 26:
                            for j in range(i):
                                if dataset['year'][j] == dataset['year'][i]:
                                        if dataset['month'][j] == dataset['month'][i]:
                                            if dataset['day'][j] == dataset['day'][i]:
                                                dataset["Suhu"][i]= dataset["Suhu"][j]
                        case 27:
                            for j in range(i):
                                if dataset['year'][j] == dataset['year'][i]:
                                        if dataset['month'][j] == dataset['month'][i]:
                                            if dataset['day'][j] == dataset['day'][i]:
                                                dataset["Suhu"][i]= dataset["Suhu"][j]
                        case 28:
                            for j in range(i):
                                if dataset['year'][j] == dataset['year'][i]:
                                        if dataset['month'][j] == dataset['month'][i]:
                                            if dataset['day'][j] == dataset['day'][i]:
                                                dataset["Suhu"][i]= dataset["Suhu"][j]
                        case 29:
                            for j in range(i):
                                if dataset['year'][j] == dataset['year'][i]:
                                        if dataset['month'][j] == dataset['month'][i]:
                                            if dataset['day'][j] == dataset['day'][i]:
                                                dataset["Suhu"][i]= dataset["Suhu"][j]
                        case 30:
                            for j in range(i):
                                if dataset['year'][j] == dataset['year'][i]:
                                        if dataset['month'][j] == dataset['month'][i]:
                                            if dataset['day'][j] == dataset['day'][i]:
                                                dataset["Suhu"][i]= dataset["Suhu"][j]
                        case 31:
                            for j in range(i):
                                if dataset['year'][j] == dataset['year'][i]:
                                        if dataset['month'][j] == dataset['month'][i]:
                                            if dataset['day'][j] == dataset['day'][i]:
                                                dataset["Suhu"][i]= dataset["Suhu"][j]
                case 2:
                    dataset["Suhu"][i] = round(random.uniform(23.3, 34.4),1)
                    match dataset['day'][i]:
                        case 1:
                           for j in range(i):
                                if dataset['year'][j] == dataset['year'][i]:
                                        if dataset['month'][j] == dataset['month'][i]:
                                            if dataset['day'][j] == dataset['day'][i]:
                                                dataset["Suhu"][i]= dataset["Suhu"][j]
                        case 2:
                            for j in range(i):
                                if dataset['year'][j] == dataset['year'][i]:
                                        if dataset['month'][j] == dataset['month'][i]:
                                            if dataset['day'][j] == dataset['day'][i]:
                                                dataset["Suhu"][i]= dataset["Suhu"][j]
                        case 3:
                            for j in range(i):
                                if dataset['year'][j] == dataset['year'][i]:
                                        if dataset['month'][j] == dataset['month'][i]:
                                            if dataset['day'][j] == dataset['day'][i]:
                                                dataset["Suhu"][i]= dataset["Suhu"][j]
                        case 4:
                             for j in range(i):
                                if dataset['year'][j] == dataset['year'][i]:
                                        if dataset['month'][j] == dataset['month'][i]:
                                            if dataset['day'][j] == dataset['day'][i]:
                                                dataset["Suhu"][i]= dataset["Suhu"][j]
                        case 5:
                             for j in range(i):
                                if dataset['year'][j] == dataset['year'][i]:
                                        if dataset['month'][j] == dataset['month'][i]:
                                            if dataset['day'][j] == dataset['day'][i]:
                                                dataset["Suhu"][i]= dataset["Suhu"][j]
                        case 6:
                            for j in range(i):
                                if dataset['year'][j] == dataset['year'][i]:
                                        if dataset['month'][j] == dataset['month'][i]:
                                            if dataset['day'][j] == dataset['day'][i]:
                                                dataset["Suhu"][i]= dataset["Suhu"][j]
                        case 7:
                            for j in range(i):
                                if dataset['year'][j] == dataset['year'][i]:
                                        if dataset['month'][j] == dataset['month'][i]:
                                            if dataset['day'][j] == dataset['day'][i]:
                                                dataset["Suhu"][i]= dataset["Suhu"][j]
                        case 8:
                            for j in range(i):
                                if dataset['year'][j] == dataset['year'][i]:
                                        if dataset['month'][j] == dataset['month'][i]:
                                            if dataset['day'][j] == dataset['day'][i]:
                                                dataset["Suhu"][i]= dataset["Suhu"][j]
                        case 9:
                            for j in range(i):
                                if dataset['year'][j] == dataset['year'][i]:
                                        if dataset['month'][j] == dataset['month'][i]:
                                            if dataset['day'][j] == dataset['day'][i]:
                                                dataset["Suhu"][i]= dataset["Suhu"][j]
                        case 10:
                            for j in range(i):
                                if dataset['year'][j] == dataset['year'][i]:
                                        if dataset['month'][j] == dataset['month'][i]:
                                            if dataset['day'][j] == dataset['day'][i]:
                                                dataset["Suhu"][i]= dataset["Suhu"][j]
                        case 11:
                            for j in range(i):
                                if dataset['year'][j] == dataset['year'][i]:
                                        if dataset['month'][j] == dataset['month'][i]:
                                            if dataset['day'][j] == dataset['day'][i]:
                                                dataset["Suhu"][i]= dataset["Suhu"][j]
                        case 12:
                            for j in range(i):
                                if dataset['year'][j] == dataset['year'][i]:
                                        if dataset['month'][j] == dataset['month'][i]:
                                            if dataset['day'][j] == dataset['day'][i]:
                                                dataset["Suhu"][i]= dataset["Suhu"][j]
                        case 13:
                            for j in range(i):
                                if dataset['year'][j] == dataset['year'][i]:
                                        if dataset['month'][j] == dataset['month'][i]:
                                            if dataset['day'][j] == dataset['day'][i]:
                                                dataset["Suhu"][i]= dataset["Suhu"][j]
                        case 14:
                            for j in range(i):
                                if dataset['year'][j] == dataset['year'][i]:
                                        if dataset['month'][j] == dataset['month'][i]:
                                            if dataset['day'][j] == dataset['day'][i]:
                                                dataset["Suhu"][i]= dataset["Suhu"][j]
                        case 15:
                            for j in range(i):
                                if dataset['year'][j] == dataset['year'][i]:
                                        if dataset['month'][j] == dataset['month'][i]:
                                            if dataset['day'][j] == dataset['day'][i]:
                                                dataset["Suhu"][i]= dataset["Suhu"][j]
                        case 16:
                            for j in range(i):
                                if dataset['year'][j] == dataset['year'][i]:
                                        if dataset['month'][j] == dataset['month'][i]:
                                            if dataset['day'][j] == dataset['day'][i]:
                                                dataset["Suhu"][i]= dataset["Suhu"][j]
                        case 17:
                            for j in range(i):
                                if dataset['year'][j] == dataset['year'][i]:
                                        if dataset['month'][j] == dataset['month'][i]:
                                            if dataset['day'][j] == dataset['day'][i]:
                                                dataset["Suhu"][i]= dataset["Suhu"][j]
                        case 18:
                            for j in range(i):
                                if dataset['year'][j] == dataset['year'][i]:
                                        if dataset['month'][j] == dataset['month'][i]:
                                            if dataset['day'][j] == dataset['day'][i]:
                                                dataset["Suhu"][i]= dataset["Suhu"][j]
                        case 19:
                            for j in range(i):
                                if dataset['year'][j] == dataset['year'][i]:
                                        if dataset['month'][j] == dataset['month'][i]:
                                            if dataset['day'][j] == dataset['day'][i]:
                                                dataset["Suhu"][i]= dataset["Suhu"][j]
                        case 20:
                            for j in range(i):
                                if dataset['year'][j] == dataset['year'][i]:
                                        if dataset['month'][j] == dataset['month'][i]:
                                            if dataset['day'][j] == dataset['day'][i]:
                                                dataset["Suhu"][i]= dataset["Suhu"][j]
                        case 21:
                            for j in range(i):
                                if dataset['year'][j] == dataset['year'][i]:
                                        if dataset['month'][j] == dataset['month'][i]:
                                            if dataset['day'][j] == dataset['day'][i]:
                                                dataset["Suhu"][i]= dataset["Suhu"][j]
                        case 22:
                            for j in range(i):
                                if dataset['year'][j] == dataset['year'][i]:
                                        if dataset['month'][j] == dataset['month'][i]:
                                            if dataset['day'][j] == dataset['day'][i]:
                                                dataset["Suhu"][i]= dataset["Suhu"][j]
                        case 23:
                            for j in range(i):
                                if dataset['year'][j] == dataset['year'][i]:
                                        if dataset['month'][j] == dataset['month'][i]:
                                            if dataset['day'][j] == dataset['day'][i]:
                                                dataset["Suhu"][i]= dataset["Suhu"][j]
                        case 24:
                            for j in range(i):
                                if dataset['year'][j] == dataset['year'][i]:
                                        if dataset['month'][j] == dataset['month'][i]:
                                            if dataset['day'][j] == dataset['day'][i]:
                                                dataset["Suhu"][i]= dataset["Suhu"][j]
                        case 25:
                            for j in range(i):
                                if dataset['year'][j] == dataset['year'][i]:
                                        if dataset['month'][j] == dataset['month'][i]:
                                            if dataset['day'][j] == dataset['day'][i]:
                                                dataset["Suhu"][i]= dataset["Suhu"][j]
                        case 26:
                            for j in range(i):
                                if dataset['year'][j] == dataset['year'][i]:
                                        if dataset['month'][j] == dataset['month'][i]:
                                            if dataset['day'][j] == dataset['day'][i]:
                                                dataset["Suhu"][i]= dataset["Suhu"][j]
                        case 27:
                            for j in range(i):
                                if dataset['year'][j] == dataset['year'][i]:
                                        if dataset['month'][j] == dataset['month'][i]:
                                            if dataset['day'][j] == dataset['day'][i]:
                                                dataset["Suhu"][i]= dataset["Suhu"][j]
                        case 28:
                            for j in range(i):
                                if dataset['year'][j] == dataset['year'][i]:
                                        if dataset['month'][j] == dataset['month'][i]:
                                            if dataset['day'][j] == dataset['day'][i]:
                                                dataset["Suhu"][i]= dataset["Suhu"][j]
                        case 29:
                            for j in range(i):
                                if dataset['year'][j] == dataset['year'][i]:
                                        if dataset['month'][j] == dataset['month'][i]:
                                            if dataset['day'][j] == dataset['day'][i]:
                                                dataset["Suhu"][i]= dataset["Suhu"][j]
                        case 30:
                            for j in range(i):
                                if dataset['year'][j] == dataset['year'][i]:
                                        if dataset['month'][j] == dataset['month'][i]:
                                            if dataset['day'][j] == dataset['day'][i]:
                                                dataset["Suhu"][i]= dataset["Suhu"][j]
                        case 31:
                            for j in range(i):
                                if dataset['year'][j] == dataset['year'][i]:
                                        if dataset['month'][j] == dataset['month'][i]:
                                            if dataset['day'][j] == dataset['day'][i]:
                                                dataset["Suhu"][i]= dataset["Suhu"][j]
                case 3:
                    dataset["Suhu"][i] = round(random.uniform(23.8, 32.9),1)
                    match dataset['day'][i]:
                        case 1:
                           for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2022][dataset["day"]==1][dataset["month"]==3][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 2:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2022][dataset["day"]==2][dataset["month"]==3][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 3:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2022][dataset["day"]==3][dataset["month"]==3][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 4:
                             for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2022][dataset["day"]==4][dataset["month"]==3][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 5:
                             for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2022][dataset["day"]==5][dataset["month"]==3][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 6:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2022][dataset["day"]==6][dataset["month"]==3][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 7:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2022][dataset["day"]==7][dataset["month"]==3][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 8:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2022][dataset["day"]==8][dataset["month"]==3][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 9:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2022][dataset["day"]==9][dataset["month"]==3][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 10:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2022][dataset["day"]==10][dataset["month"]==3][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 11:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2022][dataset["day"]==11][dataset["month"]==3][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 12:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2022][dataset["day"]==12][dataset["month"]==3][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 13:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2022][dataset["day"]==13][dataset["month"]==3][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 14:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2022][dataset["day"]==14][dataset["month"]==3][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 15:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2022][dataset["day"]==15][dataset["month"]==3][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 16:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2022][dataset["day"]==16][dataset["month"]==3][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 17:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2022][dataset["day"]==17][dataset["month"]==3][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 18:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2022][dataset["day"]==18][dataset["month"]==3][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 19:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2022][dataset["day"]==19][dataset["month"]==3][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 20:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2022][dataset["day"]==20][dataset["month"]==3][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 21:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2022][dataset["day"]==21][dataset["month"]==3][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 22:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2022][dataset["day"]==22][dataset["month"]==3][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 23:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2022][dataset["day"]==23][dataset["month"]==3][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 24:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2022][dataset["day"]==24][dataset["month"]==3][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 25:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2022][dataset["day"]==25][dataset["month"]==3][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 26:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2022][dataset["day"]==26][dataset["month"]==3][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 27:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2022][dataset["day"]==27][dataset["month"]==3][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 28:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2022][dataset["day"]==28][dataset["month"]==3][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 29:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2022][dataset["day"]==29][dataset["month"]==3][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 30:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2022][dataset["day"]==30][dataset["month"]==3][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 31:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2022][dataset["day"]==31][dataset["month"]==3][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                case 4:
                    dataset["Suhu"][i] = round(random.uniform(23.4, 35.2),1)
                    match dataset['day'][i]:
                        case 1:
                           for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2022][dataset["day"]==1][dataset["month"]==4][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 2:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2022][dataset["day"]==2][dataset["month"]==4][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 3:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2022][dataset["day"]==3][dataset["month"]==4][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 4:
                             for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2022][dataset["day"]==4][dataset["month"]==4][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 5:
                             for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2022][dataset["day"]==5][dataset["month"]==4][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 6:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2022][dataset["day"]==6][dataset["month"]==4][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 7:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2022][dataset["day"]==7][dataset["month"]==4][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 8:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2022][dataset["day"]==8][dataset["month"]==4][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 9:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2022][dataset["day"]==9][dataset["month"]==4][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 10:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2022][dataset["day"]==10][dataset["month"]==4][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 11:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2022][dataset["day"]==11][dataset["month"]==4][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 12:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2022][dataset["day"]==12][dataset["month"]==4][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 13:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2022][dataset["day"]==13][dataset["month"]==4][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 14:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2022][dataset["day"]==14][dataset["month"]==4][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 15:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2022][dataset["day"]==15][dataset["month"]==4][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 16:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2022][dataset["day"]==16][dataset["month"]==4][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 17:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2022][dataset["day"]==17][dataset["month"]==4][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 18:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2022][dataset["day"]==18][dataset["month"]==4][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 19:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2022][dataset["day"]==19][dataset["month"]==4][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 20:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2022][dataset["day"]==20][dataset["month"]==4][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 21:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2022][dataset["day"]==21][dataset["month"]==4][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 22:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2022][dataset["day"]==22][dataset["month"]==4][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 23:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2022][dataset["day"]==23][dataset["month"]==4][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 24:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2022][dataset["day"]==24][dataset["month"]==4][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 25:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2022][dataset["day"]==25][dataset["month"]==4][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 26:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2022][dataset["day"]==26][dataset["month"]==4][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 27:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2022][dataset["day"]==27][dataset["month"]==4][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 28:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2022][dataset["day"]==28][dataset["month"]==4][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 29:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2022][dataset["day"]==29][dataset["month"]==4][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 30:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2022][dataset["day"]==30][dataset["month"]==4][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 31:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2022][dataset["day"]==31][dataset["month"]==4][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                case 5:
                    dataset["Suhu"][i] = round(random.uniform(22.9, 34.6),1)
                    match dataset['day'][i]:
                        case 1:
                           for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2022][dataset["day"]==1][dataset["month"]==5][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 2:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2022][dataset["day"]==2][dataset["month"]==5][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 3:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2022][dataset["day"]==3][dataset["month"]==5][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 4:
                             for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2022][dataset["day"]==4][dataset["month"]==5][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 5:
                             for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2022][dataset["day"]==5][dataset["month"]==5][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 6:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2022][dataset["day"]==6][dataset["month"]==5][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 7:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2022][dataset["day"]==7][dataset["month"]==5][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 8:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2022][dataset["day"]==8][dataset["month"]==5][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 9:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2022][dataset["day"]==9][dataset["month"]==5][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 10:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2022][dataset["day"]==10][dataset["month"]==5][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 11:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2022][dataset["day"]==11][dataset["month"]==5][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 12:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2022][dataset["day"]==12][dataset["month"]==5][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 13:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2022][dataset["day"]==13][dataset["month"]==5][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 14:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2022][dataset["day"]==14][dataset["month"]==5][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 15:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2022][dataset["day"]==15][dataset["month"]==5][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 16:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2022][dataset["day"]==16][dataset["month"]==5][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 17:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2022][dataset["day"]==17][dataset["month"]==5][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 18:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2022][dataset["day"]==18][dataset["month"]==5][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 19:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2022][dataset["day"]==19][dataset["month"]==5][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 20:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2022][dataset["day"]==20][dataset["month"]==5][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 21:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2022][dataset["day"]==21][dataset["month"]==5][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 22:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2022][dataset["day"]==22][dataset["month"]==5][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 23:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2022][dataset["day"]==23][dataset["month"]==5][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 24:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2022][dataset["day"]==24][dataset["month"]==5][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 25:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2022][dataset["day"]==25][dataset["month"]==5][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 26:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2022][dataset["day"]==26][dataset["month"]==5][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 27:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2022][dataset["day"]==27][dataset["month"]==5][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 28:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2022][dataset["day"]==28][dataset["month"]==5][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 29:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2022][dataset["day"]==29][dataset["month"]==5][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 30:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2022][dataset["day"]==30][dataset["month"]==5][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 31:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2022][dataset["day"]==31][dataset["month"]==5][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                case 6:
                    dataset["Suhu"][i] = round(random.uniform(21.6, 34),1)
                    match dataset['day'][i]:
                        case 1:
                           for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2022][dataset["day"]==1][dataset["month"]==6][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 2:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2022][dataset["day"]==2][dataset["month"]==6][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 3:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2022][dataset["day"]==3][dataset["month"]==6][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 4:
                             for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2022][dataset["day"]==4][dataset["month"]==6][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 5:
                             for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2022][dataset["day"]==5][dataset["month"]==6][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 6:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2022][dataset["day"]==6][dataset["month"]==6][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 7:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2022][dataset["day"]==7][dataset["month"]==6][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 8:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2022][dataset["day"]==8][dataset["month"]==6][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 9:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2022][dataset["day"]==9][dataset["month"]==6][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 10:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2022][dataset["day"]==10][dataset["month"]==6][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 11:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2022][dataset["day"]==11][dataset["month"]==6][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 12:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2022][dataset["day"]==12][dataset["month"]==6][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 13:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2022][dataset["day"]==13][dataset["month"]==6][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 14:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2022][dataset["day"]==14][dataset["month"]==6][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 15:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2022][dataset["day"]==15][dataset["month"]==6][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 16:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2022][dataset["day"]==16][dataset["month"]==6][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 17:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2022][dataset["day"]==17][dataset["month"]==6][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 18:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2022][dataset["day"]==18][dataset["month"]==6][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 19:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2022][dataset["day"]==19][dataset["month"]==6][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 20:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2022][dataset["day"]==20][dataset["month"]==6][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 21:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2022][dataset["day"]==21][dataset["month"]==6][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 22:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2022][dataset["day"]==22][dataset["month"]==6][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 23:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2022][dataset["day"]==23][dataset["month"]==6][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 24:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2022][dataset["day"]==24][dataset["month"]==6][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 25:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2022][dataset["day"]==25][dataset["month"]==6][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 26:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2022][dataset["day"]==26][dataset["month"]==6][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 27:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2022][dataset["day"]==27][dataset["month"]==6][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 28:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2022][dataset["day"]==28][dataset["month"]==6][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 29:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2022][dataset["day"]==29][dataset["month"]==6][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 30:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2022][dataset["day"]==30][dataset["month"]==6][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 31:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2022][dataset["day"]==31][dataset["month"]==6][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                case 7:
                    dataset["Suhu"][i] = round(random.uniform(21.7, 34.6),1)
                    match dataset['day'][i]:
                        case 1:
                           for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2022][dataset["day"]==1][dataset["month"]==7][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 2:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2022][dataset["day"]==2][dataset["month"]==7][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 3:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2022][dataset["day"]==3][dataset["month"]==7][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 4:
                             for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2022][dataset["day"]==4][dataset["month"]==7][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 5:
                             for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2022][dataset["day"]==5][dataset["month"]==7][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 6:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2022][dataset["day"]==6][dataset["month"]==7][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 7:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2022][dataset["day"]==7][dataset["month"]==7][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 8:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2022][dataset["day"]==8][dataset["month"]==7][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 9:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2022][dataset["day"]==9][dataset["month"]==7][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 10:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2022][dataset["day"]==10][dataset["month"]==7][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 11:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2022][dataset["day"]==11][dataset["month"]==7][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 12:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2022][dataset["day"]==12][dataset["month"]==7][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 13:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2022][dataset["day"]==13][dataset["month"]==7][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 14:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2022][dataset["day"]==14][dataset["month"]==7][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 15:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2022][dataset["day"]==15][dataset["month"]==7][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 16:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2022][dataset["day"]==16][dataset["month"]==7][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 17:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2022][dataset["day"]==17][dataset["month"]==7][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 18:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2022][dataset["day"]==18][dataset["month"]==7][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 19:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2022][dataset["day"]==19][dataset["month"]==7][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 20:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2022][dataset["day"]==20][dataset["month"]==7][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 21:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2022][dataset["day"]==21][dataset["month"]==7][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 22:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2022][dataset["day"]==22][dataset["month"]==7][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 23:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2022][dataset["day"]==23][dataset["month"]==7][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 24:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2022][dataset["day"]==24][dataset["month"]==7][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 25:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2022][dataset["day"]==25][dataset["month"]==7][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 26:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2022][dataset["day"]==26][dataset["month"]==7][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 27:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2022][dataset["day"]==27][dataset["month"]==7][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 28:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2022][dataset["day"]==28][dataset["month"]==7][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 29:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2022][dataset["day"]==29][dataset["month"]==7][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 30:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2022][dataset["day"]==30][dataset["month"]==7][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 31:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2022][dataset["day"]==31][dataset["month"]==7][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                case 8:
                    dataset["Suhu"][i] = round(random.uniform(22.8, 34.6),1)
                    match dataset['day'][i]:
                        case 1:
                           for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2022][dataset["day"]==1][dataset["month"]==8][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 2:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2022][dataset["day"]==2][dataset["month"]==8][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 3:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2022][dataset["day"]==3][dataset["month"]==8][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 4:
                             for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2022][dataset["day"]==4][dataset["month"]==8][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 5:
                             for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2022][dataset["day"]==5][dataset["month"]==8][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 6:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2022][dataset["day"]==6][dataset["month"]==8][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 7:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2022][dataset["day"]==7][dataset["month"]==8][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 8:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2022][dataset["day"]==8][dataset["month"]==8][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 9:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2022][dataset["day"]==9][dataset["month"]==8][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 10:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2022][dataset["day"]==10][dataset["month"]==8][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 11:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2022][dataset["day"]==11][dataset["month"]==8][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 12:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2022][dataset["day"]==12][dataset["month"]==8][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 13:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2022][dataset["day"]==13][dataset["month"]==8][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 14:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2022][dataset["day"]==14][dataset["month"]==8][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 15:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2022][dataset["day"]==15][dataset["month"]==8][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 16:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2022][dataset["day"]==16][dataset["month"]==8][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 17:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2022][dataset["day"]==17][dataset["month"]==8][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 18:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2022][dataset["day"]==18][dataset["month"]==8][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 19:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2022][dataset["day"]==19][dataset["month"]==8][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 20:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2022][dataset["day"]==20][dataset["month"]==8][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 21:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2022][dataset["day"]==21][dataset["month"]==8][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 22:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2022][dataset["day"]==22][dataset["month"]==8][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 23:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2022][dataset["day"]==23][dataset["month"]==8][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 24:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2022][dataset["day"]==24][dataset["month"]==8][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 25:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2022][dataset["day"]==25][dataset["month"]==8][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 26:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2022][dataset["day"]==26][dataset["month"]==8][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 27:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2022][dataset["day"]==27][dataset["month"]==8][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 28:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2022][dataset["day"]==28][dataset["month"]==8][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 29:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2022][dataset["day"]==29][dataset["month"]==8][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 30:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2022][dataset["day"]==30][dataset["month"]==8][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 31:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2022][dataset["day"]==31][dataset["month"]==8][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                case 9:
                    dataset["Suhu"][i] = round(random.uniform(23,4, 36),1)
                    match dataset['day'][i]:
                        case 1:
                           for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2022][dataset["day"]==1][dataset["month"]==9][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 2:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2022][dataset["day"]==2][dataset["month"]==9][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 3:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2022][dataset["day"]==3][dataset["month"]==9][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 4:
                             for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2022][dataset["day"]==4][dataset["month"]==9][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 5:
                             for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2022][dataset["day"]==5][dataset["month"]==9][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 6:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2022][dataset["day"]==6][dataset["month"]==9][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 7:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2022][dataset["day"]==7][dataset["month"]==9][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 8:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2022][dataset["day"]==8][dataset["month"]==9][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 9:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2022][dataset["day"]==9][dataset["month"]==9][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 10:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2022][dataset["day"]==10][dataset["month"]==9][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 11:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2022][dataset["day"]==11][dataset["month"]==9][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 12:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2022][dataset["day"]==12][dataset["month"]==9][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 13:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2022][dataset["day"]==13][dataset["month"]==9][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 14:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2022][dataset["day"]==14][dataset["month"]==9][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 15:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2022][dataset["day"]==15][dataset["month"]==9][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 16:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2022][dataset["day"]==16][dataset["month"]==9][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 17:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2022][dataset["day"]==17][dataset["month"]==9][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 18:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2022][dataset["day"]==18][dataset["month"]==9][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 19:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2022][dataset["day"]==19][dataset["month"]==9][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 20:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2022][dataset["day"]==20][dataset["month"]==9][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 21:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2022][dataset["day"]==21][dataset["month"]==9][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 22:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2022][dataset["day"]==22][dataset["month"]==9][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 23:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2022][dataset["day"]==23][dataset["month"]==9][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 24:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2022][dataset["day"]==24][dataset["month"]==9][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 25:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2022][dataset["day"]==25][dataset["month"]==9][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 26:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2022][dataset["day"]==26][dataset["month"]==9][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 27:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2022][dataset["day"]==27][dataset["month"]==9][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 28:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2022][dataset["day"]==28][dataset["month"]==9][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 29:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2022][dataset["day"]==29][dataset["month"]==9][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 30:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2022][dataset["day"]==30][dataset["month"]==9][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 31:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2022][dataset["day"]==31][dataset["month"]==9][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                case 10:
                    dataset["Suhu"][i] = round(random.uniform(23.4, 33,8),1)
                    match dataset['day'][i]:
                        case 1:
                           for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2022][dataset["day"]==1][dataset["month"]==10][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 2:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2022][dataset["day"]==2][dataset["month"]==10][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 3:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2022][dataset["day"]==3][dataset["month"]==10][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 4:
                             for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2022][dataset["day"]==4][dataset["month"]==10][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 5:
                             for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2022][dataset["day"]==5][dataset["month"]==10][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 6:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2022][dataset["day"]==6][dataset["month"]==10][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 7:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2022][dataset["day"]==7][dataset["month"]==10][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 8:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2022][dataset["day"]==8][dataset["month"]==10][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 9:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2022][dataset["day"]==9][dataset["month"]==10][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 10:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2022][dataset["day"]==10][dataset["month"]==10][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 11:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2022][dataset["day"]==11][dataset["month"]==10][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 12:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2022][dataset["day"]==12][dataset["month"]==10][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 13:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2022][dataset["day"]==13][dataset["month"]==10][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 14:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2022][dataset["day"]==14][dataset["month"]==10][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 15:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2022][dataset["day"]==15][dataset["month"]==10][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 16:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2022][dataset["day"]==16][dataset["month"]==10][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 17:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2022][dataset["day"]==17][dataset["month"]==10][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 18:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2022][dataset["day"]==18][dataset["month"]==10][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 19:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2022][dataset["day"]==19][dataset["month"]==10][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 20:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2022][dataset["day"]==20][dataset["month"]==10][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 21:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2022][dataset["day"]==21][dataset["month"]==10][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 22:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2022][dataset["day"]==22][dataset["month"]==10][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 23:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2022][dataset["day"]==23][dataset["month"]==10][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 24:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2022][dataset["day"]==24][dataset["month"]==10][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 25:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2022][dataset["day"]==25][dataset["month"]==10][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 26:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2022][dataset["day"]==26][dataset["month"]==10][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 27:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2022][dataset["day"]==27][dataset["month"]==10][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 28:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2022][dataset["day"]==28][dataset["month"]==10][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 29:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2022][dataset["day"]==29][dataset["month"]==10][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 30:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2022][dataset["day"]==30][dataset["month"]==10][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 31:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2022][dataset["day"]==31][dataset["month"]==10][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                case 11:
                    dataset["Suhu"][i] = round(random.uniform(23.6, 34.3),1)
                    match dataset['day'][i]:
                        case 1:
                           for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2022][dataset["day"]==1][dataset["month"]==11][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 2:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2022][dataset["day"]==2][dataset["month"]==11][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 3:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2022][dataset["day"]==3][dataset["month"]==11][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 4:
                             for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2022][dataset["day"]==4][dataset["month"]==11][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 5:
                             for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2022][dataset["day"]==5][dataset["month"]==11][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 6:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2022][dataset["day"]==6][dataset["month"]==11][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 7:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2022][dataset["day"]==7][dataset["month"]==11][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 8:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2022][dataset["day"]==8][dataset["month"]==11][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 9:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2022][dataset["day"]==9][dataset["month"]==11][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 10:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2022][dataset["day"]==10][dataset["month"]==11][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 11:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2022][dataset["day"]==11][dataset["month"]==11][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 12:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2022][dataset["day"]==12][dataset["month"]==11][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 13:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2022][dataset["day"]==13][dataset["month"]==11][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 14:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2022][dataset["day"]==14][dataset["month"]==11][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 15:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2022][dataset["day"]==15][dataset["month"]==11][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 16:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2022][dataset["day"]==16][dataset["month"]==11][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 17:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2022][dataset["day"]==17][dataset["month"]==11][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 18:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2022][dataset["day"]==18][dataset["month"]==11][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 19:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2022][dataset["day"]==19][dataset["month"]==11][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 20:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2022][dataset["day"]==20][dataset["month"]==11][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 21:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2022][dataset["day"]==21][dataset["month"]==11][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 22:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2022][dataset["day"]==22][dataset["month"]==11][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 23:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2022][dataset["day"]==23][dataset["month"]==11][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 24:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2022][dataset["day"]==24][dataset["month"]==11][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 25:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2022][dataset["day"]==25][dataset["month"]==11][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 26:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2022][dataset["day"]==26][dataset["month"]==11][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 27:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2022][dataset["day"]==27][dataset["month"]==11][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 28:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2022][dataset["day"]==28][dataset["month"]==11][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 29:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2022][dataset["day"]==29][dataset["month"]==11][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 30:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2022][dataset["day"]==30][dataset["month"]==11][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 31:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2022][dataset["day"]==31][dataset["month"]==11][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                case 12:
                    dataset["Suhu"][i] = round(random.uniform(22.8, 33.2),1)
                    match dataset['day'][i]:
                        case 1:
                           for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2022][dataset["day"]==1][dataset["month"]==12][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 2:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2022][dataset["day"]==2][dataset["month"]==12][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 3:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2022][dataset["day"]==3][dataset["month"]==12][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 4:
                             for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2022][dataset["day"]==4][dataset["month"]==12][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 5:
                             for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2022][dataset["day"]==5][dataset["month"]==12][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 6:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2022][dataset["day"]==6][dataset["month"]==12][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 7:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2022][dataset["day"]==7][dataset["month"]==12][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 8:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2022][dataset["day"]==8][dataset["month"]==12][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 9:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2022][dataset["day"]==9][dataset["month"]==12][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 10:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2022][dataset["day"]==10][dataset["month"]==12][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 11:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2022][dataset["day"]==11][dataset["month"]==12][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 12:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2022][dataset["day"]==12][dataset["month"]==12][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 13:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2022][dataset["day"]==13][dataset["month"]==12][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 14:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2022][dataset["day"]==14][dataset["month"]==12][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 15:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2022][dataset["day"]==15][dataset["month"]==12][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 16:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2022][dataset["day"]==16][dataset["month"]==12][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 17:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2022][dataset["day"]==17][dataset["month"]==12][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 18:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2022][dataset["day"]==18][dataset["month"]==12][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 19:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2022][dataset["day"]==19][dataset["month"]==12][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 20:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2022][dataset["day"]==20][dataset["month"]==12][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 21:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2022][dataset["day"]==21][dataset["month"]==12][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 22:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2022][dataset["day"]==22][dataset["month"]==12][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 23:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2022][dataset["day"]==23][dataset["month"]==12][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 24:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2022][dataset["day"]==24][dataset["month"]==12][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 25:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2022][dataset["day"]==25][dataset["month"]==12][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 26:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2022][dataset["day"]==26][dataset["month"]==12][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 27:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2022][dataset["day"]==27][dataset["month"]==12][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 28:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2022][dataset["day"]==28][dataset["month"]==12][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 29:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2022][dataset["day"]==29][dataset["month"]==12][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 30:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2022][dataset["day"]==30][dataset["month"]==12][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 31:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2022][dataset["day"]==31][dataset["month"]==12][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
        case 2023:
            match dataset["month"][i]:
                case 1:
                    dataset["Suhu"][i] = round(random.uniform(23.5, 32.6),1)
                    match dataset['day'][i]:
                        case 1:
                           for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==1][dataset["month"]==1][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 2:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==2][dataset["month"]==1][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 3:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==3][dataset["month"]==1][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 4:
                             for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==4][dataset["month"]==1][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 5:
                             for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==5][dataset["month"]==1][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 6:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==6][dataset["month"]==1][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 7:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==7][dataset["month"]==1][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 8:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==8][dataset["month"]==1][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 9:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==9][dataset["month"]==1][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 10:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==10][dataset["month"]==1][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 11:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==11][dataset["month"]==1][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 12:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==12][dataset["month"]==1][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 13:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==13][dataset["month"]==1][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 14:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==14][dataset["month"]==1][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 15:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==15][dataset["month"]==1][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 16:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==16][dataset["month"]==1][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 17:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==17][dataset["month"]==1][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 18:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==18][dataset["month"]==1][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 19:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==19][dataset["month"]==1][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 20:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==20][dataset["month"]==1][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 21:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==21][dataset["month"]==1][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 22:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==22][dataset["month"]==1][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 23:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==23][dataset["month"]==1][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 24:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==24][dataset["month"]==1][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 25:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==25][dataset["month"]==1][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 26:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==26][dataset["month"]==1][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 27:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==27][dataset["month"]==1][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 28:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==28][dataset["month"]==1][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 29:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==29][dataset["month"]==1][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 30:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==30][dataset["month"]==1][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 31:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==31][dataset["month"]==1][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                case 2:
                    dataset["Suhu"][i] = round(random.uniform(23.3, 34.4),1)
                    match dataset['day'][i]:
                        case 1:
                           for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==1][dataset["month"]==2][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 2:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==2][dataset["month"]==2][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 3:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==3][dataset["month"]==2][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 4:
                             for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==4][dataset["month"]==2][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 5:
                             for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==5][dataset["month"]==2][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 6:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==6][dataset["month"]==2][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 7:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==7][dataset["month"]==2][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 8:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==8][dataset["month"]==2][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 9:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==9][dataset["month"]==2][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 10:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==10][dataset["month"]==2][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 11:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==11][dataset["month"]==2][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 12:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==12][dataset["month"]==2][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 13:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==13][dataset["month"]==2][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 14:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==14][dataset["month"]==2][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 15:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==15][dataset["month"]==2][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 16:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==16][dataset["month"]==2][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 17:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==17][dataset["month"]==2][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 18:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==18][dataset["month"]==2][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 19:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==19][dataset["month"]==2][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 20:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==20][dataset["month"]==2][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 21:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==21][dataset["month"]==2][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 22:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==22][dataset["month"]==2][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 23:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==23][dataset["month"]==2][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 24:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==24][dataset["month"]==2][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 25:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==25][dataset["month"]==2][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 26:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==26][dataset["month"]==2][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 27:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==27][dataset["month"]==2][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 28:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==28][dataset["month"]==2][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 29:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==29][dataset["month"]==2][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 30:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==30][dataset["month"]==2][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 31:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==31][dataset["month"]==2][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                case 3:
                    dataset["Suhu"][i] = round(random.uniform(23.8, 32.9),1)
                    match dataset['day'][i]:
                        case 1:
                           for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==1][dataset["month"]==3][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 2:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==2][dataset["month"]==3][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 3:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==3][dataset["month"]==3][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 4:
                             for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==4][dataset["month"]==3][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 5:
                             for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==5][dataset["month"]==3][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 6:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==6][dataset["month"]==3][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 7:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==7][dataset["month"]==3][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 8:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==8][dataset["month"]==3][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 9:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==9][dataset["month"]==3][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 10:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==10][dataset["month"]==3][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 11:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==11][dataset["month"]==3][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 12:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==12][dataset["month"]==3][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 13:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==13][dataset["month"]==3][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 14:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==14][dataset["month"]==3][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 15:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==15][dataset["month"]==3][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 16:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==16][dataset["month"]==3][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 17:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==17][dataset["month"]==3][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 18:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==18][dataset["month"]==3][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 19:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==19][dataset["month"]==3][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 20:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==20][dataset["month"]==3][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 21:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==21][dataset["month"]==3][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 22:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==22][dataset["month"]==3][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 23:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==23][dataset["month"]==3][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 24:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==24][dataset["month"]==3][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 25:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==25][dataset["month"]==3][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 26:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==26][dataset["month"]==3][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 27:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==27][dataset["month"]==3][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 28:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==28][dataset["month"]==3][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 29:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==29][dataset["month"]==3][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 30:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==30][dataset["month"]==3][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 31:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==31][dataset["month"]==3][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                case 4:
                    dataset["Suhu"][i] = round(random.uniform(23.4, 35.2),1)
                    match dataset['day'][i]:
                        case 1:
                           for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==1][dataset["month"]==4][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 2:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==2][dataset["month"]==4][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 3:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==3][dataset["month"]==4][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 4:
                             for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==4][dataset["month"]==4][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 5:
                             for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==5][dataset["month"]==4][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 6:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==6][dataset["month"]==4][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 7:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==7][dataset["month"]==4][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 8:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==8][dataset["month"]==4][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 9:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==9][dataset["month"]==4][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 10:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==10][dataset["month"]==4][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 11:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==11][dataset["month"]==4][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 12:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==12][dataset["month"]==4][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 13:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==13][dataset["month"]==4][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 14:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==14][dataset["month"]==4][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 15:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==15][dataset["month"]==4][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 16:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==16][dataset["month"]==4][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 17:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==17][dataset["month"]==4][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 18:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==18][dataset["month"]==4][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 19:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==19][dataset["month"]==4][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 20:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==20][dataset["month"]==4][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 21:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==21][dataset["month"]==4][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 22:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==22][dataset["month"]==4][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 23:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==23][dataset["month"]==4][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 24:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==24][dataset["month"]==4][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 25:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==25][dataset["month"]==4][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 26:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==26][dataset["month"]==4][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 27:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==27][dataset["month"]==4][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 28:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==28][dataset["month"]==4][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 29:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==29][dataset["month"]==4][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 30:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==30][dataset["month"]==4][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 31:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==31][dataset["month"]==4][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                case 5:
                    dataset["Suhu"][i] = round(random.uniform(22.9, 34.6),1)
                    match dataset['day'][i]:
                        case 1:
                           for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==1][dataset["month"]==5][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 2:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==2][dataset["month"]==5][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 3:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==3][dataset["month"]==5][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 4:
                             for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==4][dataset["month"]==5][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 5:
                             for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==5][dataset["month"]==5][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 6:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==6][dataset["month"]==5][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 7:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==7][dataset["month"]==5][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 8:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==8][dataset["month"]==5][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 9:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==9][dataset["month"]==5][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 10:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==10][dataset["month"]==5][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 11:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==11][dataset["month"]==5][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 12:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==12][dataset["month"]==5][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 13:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==13][dataset["month"]==5][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 14:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==14][dataset["month"]==5][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 15:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==15][dataset["month"]==5][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 16:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==16][dataset["month"]==5][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 17:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==17][dataset["month"]==5][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 18:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==18][dataset["month"]==5][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 19:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==19][dataset["month"]==5][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 20:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==20][dataset["month"]==5][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 21:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==21][dataset["month"]==5][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 22:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==22][dataset["month"]==5][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 23:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==23][dataset["month"]==5][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 24:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==24][dataset["month"]==5][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 25:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==25][dataset["month"]==5][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 26:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==26][dataset["month"]==5][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 27:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==27][dataset["month"]==5][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 28:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==28][dataset["month"]==5][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 29:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==29][dataset["month"]==5][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 30:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==30][dataset["month"]==5][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 31:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==31][dataset["month"]==5][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                case 6:
                    dataset["Suhu"][i] = round(random.uniform(21.6, 34),1)
                    match dataset['day'][i]:
                        case 1:
                           for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==1][dataset["month"]==6][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 2:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==2][dataset["month"]==6][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 3:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==3][dataset["month"]==6][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 4:
                             for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==4][dataset["month"]==6][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 5:
                             for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==5][dataset["month"]==6][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 6:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==6][dataset["month"]==6][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 7:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==7][dataset["month"]==6][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 8:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==8][dataset["month"]==6][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 9:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==9][dataset["month"]==6][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 10:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==10][dataset["month"]==6][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 11:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==11][dataset["month"]==6][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 12:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==12][dataset["month"]==6][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 13:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==13][dataset["month"]==6][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 14:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==14][dataset["month"]==6][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 15:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==15][dataset["month"]==6][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 16:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==16][dataset["month"]==6][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 17:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==17][dataset["month"]==6][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 18:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==18][dataset["month"]==6][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 19:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==19][dataset["month"]==6][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 20:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==20][dataset["month"]==6][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 21:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==21][dataset["month"]==6][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 22:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==22][dataset["month"]==6][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 23:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==23][dataset["month"]==6][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 24:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==24][dataset["month"]==6][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 25:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==25][dataset["month"]==6][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 26:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==26][dataset["month"]==6][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 27:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==27][dataset["month"]==6][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 28:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==28][dataset["month"]==6][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 29:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==29][dataset["month"]==6][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 30:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==30][dataset["month"]==6][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 31:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==31][dataset["month"]==6][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                case 7:
                    dataset["Suhu"][i] = round(random.uniform(21.7, 34.6),1)
                    match dataset['day'][i]:
                        case 1:
                           for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==1][dataset["month"]==7][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 2:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==2][dataset["month"]==7][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 3:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==3][dataset["month"]==7][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 4:
                             for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==4][dataset["month"]==7][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 5:
                             for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==5][dataset["month"]==7][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 6:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==6][dataset["month"]==7][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 7:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==7][dataset["month"]==7][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 8:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==8][dataset["month"]==7][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 9:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==9][dataset["month"]==7][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 10:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==10][dataset["month"]==7][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 11:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==11][dataset["month"]==7][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 12:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==12][dataset["month"]==7][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 13:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==13][dataset["month"]==7][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 14:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==14][dataset["month"]==7][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 15:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==15][dataset["month"]==7][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 16:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==16][dataset["month"]==7][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 17:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==17][dataset["month"]==7][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 18:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==18][dataset["month"]==7][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 19:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==19][dataset["month"]==7][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 20:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==20][dataset["month"]==7][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 21:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==21][dataset["month"]==7][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 22:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==22][dataset["month"]==7][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 23:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==23][dataset["month"]==7][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 24:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==24][dataset["month"]==7][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 25:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==25][dataset["month"]==7][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 26:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==26][dataset["month"]==7][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 27:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==27][dataset["month"]==7][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 28:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==28][dataset["month"]==7][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 29:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==29][dataset["month"]==7][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 30:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==30][dataset["month"]==7][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 31:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==31][dataset["month"]==7][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                case 8:
                    dataset["Suhu"][i] = round(random.uniform(22.8, 34.6),1)
                    match dataset['day'][i]:
                        case 1:
                           for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==1][dataset["month"]==8][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 2:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==2][dataset["month"]==8][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 3:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==3][dataset["month"]==8][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 4:
                             for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==4][dataset["month"]==8][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 5:
                             for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==5][dataset["month"]==8][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 6:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==6][dataset["month"]==8][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 7:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==7][dataset["month"]==8][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 8:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==8][dataset["month"]==8][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 9:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==9][dataset["month"]==8][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 10:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==10][dataset["month"]==8][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 11:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==11][dataset["month"]==8][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 12:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==12][dataset["month"]==8][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 13:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==13][dataset["month"]==8][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 14:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==14][dataset["month"]==8][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 15:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==15][dataset["month"]==8][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 16:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==16][dataset["month"]==8][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 17:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==17][dataset["month"]==8][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 18:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==18][dataset["month"]==8][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 19:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==19][dataset["month"]==8][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 20:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==20][dataset["month"]==8][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 21:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==21][dataset["month"]==8][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 22:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==22][dataset["month"]==8][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 23:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==23][dataset["month"]==8][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 24:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==24][dataset["month"]==8][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 25:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==25][dataset["month"]==8][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 26:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==26][dataset["month"]==8][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 27:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==27][dataset["month"]==8][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 28:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==28][dataset["month"]==8][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 29:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==29][dataset["month"]==8][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 30:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==30][dataset["month"]==8][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 31:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==31][dataset["month"]==8][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                case 9:
                    dataset["Suhu"][i] = round(random.uniform(23,4, 36),1)
                    match dataset['day'][i]:
                        case 1:
                           for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==1][dataset["month"]==9][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 2:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==2][dataset["month"]==9][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 3:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==3][dataset["month"]==9][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 4:
                             for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==4][dataset["month"]==9][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 5:
                             for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==5][dataset["month"]==9][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 6:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==6][dataset["month"]==9][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 7:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==7][dataset["month"]==9][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 8:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==8][dataset["month"]==9][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 9:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==9][dataset["month"]==9][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 10:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==10][dataset["month"]==9][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 11:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==11][dataset["month"]==9][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 12:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==12][dataset["month"]==9][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 13:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==13][dataset["month"]==9][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 14:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==14][dataset["month"]==9][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 15:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==15][dataset["month"]==9][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 16:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==16][dataset["month"]==9][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 17:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==17][dataset["month"]==9][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 18:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==18][dataset["month"]==9][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 19:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==19][dataset["month"]==9][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 20:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==20][dataset["month"]==9][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 21:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==21][dataset["month"]==9][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 22:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==22][dataset["month"]==9][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 23:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==23][dataset["month"]==9][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 24:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==24][dataset["month"]==9][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 25:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==25][dataset["month"]==9][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 26:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==26][dataset["month"]==9][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 27:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==27][dataset["month"]==9][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 28:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==28][dataset["month"]==9][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 29:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==29][dataset["month"]==9][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 30:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==30][dataset["month"]==9][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 31:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==31][dataset["month"]==9][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                case 10:
                    dataset["Suhu"][i] = round(random.uniform(23.4, 33,8),1)
                    match dataset['day'][i]:
                        case 1:
                           for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==1][dataset["month"]==10][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 2:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==2][dataset["month"]==10][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 3:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==3][dataset["month"]==10][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 4:
                             for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==4][dataset["month"]==10][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 5:
                             for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==5][dataset["month"]==10][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 6:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==6][dataset["month"]==10][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 7:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==7][dataset["month"]==10][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 8:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==8][dataset["month"]==10][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 9:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==9][dataset["month"]==10][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 10:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==10][dataset["month"]==10][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 11:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==11][dataset["month"]==10][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 12:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==12][dataset["month"]==10][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 13:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==13][dataset["month"]==10][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 14:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==14][dataset["month"]==10][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 15:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==15][dataset["month"]==10][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 16:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==16][dataset["month"]==10][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 17:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==17][dataset["month"]==10][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 18:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==18][dataset["month"]==10][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 19:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==19][dataset["month"]==10][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 20:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==20][dataset["month"]==10][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 21:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==21][dataset["month"]==10][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 22:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==22][dataset["month"]==10][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 23:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==23][dataset["month"]==10][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 24:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==24][dataset["month"]==10][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 25:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==25][dataset["month"]==10][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 26:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==26][dataset["month"]==10][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 27:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==27][dataset["month"]==10][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 28:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==28][dataset["month"]==10][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 29:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==29][dataset["month"]==10][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 30:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==30][dataset["month"]==10][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 31:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==31][dataset["month"]==10][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                case 11:
                    dataset["Suhu"][i] = round(random.uniform(23.6, 34.3),1)
                    match dataset['day'][i]:
                        case 1:
                           for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==1][dataset["month"]==11][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 2:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==2][dataset["month"]==11][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 3:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==3][dataset["month"]==11][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 4:
                             for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==4][dataset["month"]==11][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 5:
                             for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==5][dataset["month"]==11][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 6:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==6][dataset["month"]==11][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 7:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==7][dataset["month"]==11][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 8:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==8][dataset["month"]==11][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 9:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==9][dataset["month"]==11][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 10:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==10][dataset["month"]==11][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 11:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==11][dataset["month"]==11][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 12:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==12][dataset["month"]==11][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 13:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==13][dataset["month"]==11][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 14:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==14][dataset["month"]==11][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 15:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==15][dataset["month"]==11][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 16:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==16][dataset["month"]==11][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 17:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==17][dataset["month"]==11][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 18:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==18][dataset["month"]==11][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 19:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==19][dataset["month"]==11][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 20:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==20][dataset["month"]==11][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 21:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==21][dataset["month"]==11][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 22:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==22][dataset["month"]==11][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 23:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==23][dataset["month"]==11][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 24:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==24][dataset["month"]==11][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 25:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==25][dataset["month"]==11][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 26:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==26][dataset["month"]==11][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 27:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==27][dataset["month"]==11][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 28:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==28][dataset["month"]==11][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 29:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==29][dataset["month"]==11][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 30:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==30][dataset["month"]==11][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 31:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==31][dataset["month"]==11][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                case 12:
                    dataset["Suhu"][i] = round(random.uniform(22.8, 33.2),1)
                    match dataset['day'][i]:
                        case 1:
                           for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==1][dataset["month"]==12][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 2:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==2][dataset["month"]==12][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 3:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==3][dataset["month"]==12][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 4:
                             for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==4][dataset["month"]==12][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 5:
                             for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==5][dataset["month"]==12][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 6:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==6][dataset["month"]==12][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 7:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==7][dataset["month"]==12][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 8:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==8][dataset["month"]==12][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 9:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==9][dataset["month"]==12][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 10:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==10][dataset["month"]==12][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 11:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==11][dataset["month"]==12][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 12:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==12][dataset["month"]==12][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 13:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==13][dataset["month"]==12][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 14:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==14][dataset["month"]==12][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 15:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==15][dataset["month"]==12][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 16:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==16][dataset["month"]==12][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 17:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==17][dataset["month"]==12][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 18:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==18][dataset["month"]==12][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 19:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==19][dataset["month"]==12][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 20:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==20][dataset["month"]==12][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 21:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==21][dataset["month"]==12][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 22:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==22][dataset["month"]==12][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 23:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==23][dataset["month"]==12][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 24:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==24][dataset["month"]==12][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 25:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==25][dataset["month"]==12][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 26:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==26][dataset["month"]==12][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 27:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==27][dataset["month"]==12][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 28:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==28][dataset["month"]==12][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 29:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==29][dataset["month"]==12][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 30:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==30][dataset["month"]==12][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
                        case 31:
                            for j in range(i):
                                temp = dataset["Suhu"][dataset["year"]==2023][dataset["day"]==31][dataset["month"]==12][j]
                                # print(temp)
                                dataset["Suhu"][i] = temp
        case _ :
                print("COba di 2021")
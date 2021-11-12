### PLOT ###

for machine in range( decoder_data["quant_of_machines"] ):    # 10
  for operation in range( decoder_data["half_of_scheduling"] ):       # 30
    current_start_time      = start_time[machine][operation]
    current_end_time        = end_time[machine][operation]
    current_diference_time  = current_end_time - current_start_time
    #if current_diference_time > 0:
    if end_time[machine][operation] != 0 and end_time[machine][operation] - start_time[machine][operation] != 0:
      operation_id = find_machine_of_a_operation(operation)
      bar_left  = current_start_time
      bar_width = current_diference_time
      bar_color = colors[operation_id[0] - 1]
      bar_str   = operation_id

      plt.barh(y=machine, width=bar_width, height=0.5, left=bar_left, color=bar_color, edgecolor='black')
      plt.text(x=bar_left + 0.1, y=machine, s=bar_str, fontsize=8)
#
#ax.yticks(np.arange(machine + 1), np.arange(1, machine + 2))
#plt.yticks(np.arange(machine + 1), np.arange(1, machine + 2))

plt.show()
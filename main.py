import click, utils, amspy
from datetime import datetime

@click.command()
@click.option('--all', is_flag=True, help='Obfuscate using all the parameters')
@click.option('--changevariables', is_flag=True, help='Change variable names to random words from a dictionary. Dictionary words tend to not be suspicious')
@click.option('--caps', is_flag=True, help='Randomly capatalise variable/function names')
@click.option('--left2right', is_flag=True, help='Reverses strings to an array and read in reverse')
@click.option('--iphex', is_flag=True, help='Transform potential IP addresses in the code to hexaddresses')
@click.option('--comments', is_flag=True, help='Place random comments in the code to differantiate the final hash even more')
@click.option('--oneliner', is_flag=True, help='Convert the powershell into a oneliner. This will not add any comments to fill the script\r\n Note:Only advisable on smaller codebases')
@click.option('--output', default='', help='Custom output filename, default will be Obfuscated_inputfilename_datetime.ps1')
@click.argument("inputfile")
def main(all, changevariables, caps, left2right, iphex, comments, oneliner, output, inputfile):
    print('Starting AMSBye')
    utils.check_extension(inputfile)
    utils.check_file_exists(inputfile)
    utils.check_file_has_content(inputfile)
    today = datetime.now()
    output_file_name = ''
    if not output or len(output) == 0:
        output_file_name = f'Obfuscated_{inputfile.replace('.ps1', '')}_{today.strftime('%d%m%Y%H%M%S')}.ps1'
    else:
        output_file_name = output
    amspye = amspy.AMSIPye(input=inputfile, output=output_file_name)
    if changevariables or all:
        amspye.change_variable_names()
    if caps or all:
        amspye.capatalise_functions()
    if left2right or all:
        altered_variables: list[str] = amspye.left2right()
        for variable_name in altered_variables:
            amspye.replace_variables_except_first_and_second_to_join(variable_name=variable_name)
    if iphex or all:
        amspye.ip_to_hex()
    if oneliner:
        amspye.convert_to_oneliner()
    if comments or all and not oneliner:
        amspye.write_random_comments()
    amspye.write_to_output_file()
    print('Goodbye...')

if __name__ == '__main__':
    main()
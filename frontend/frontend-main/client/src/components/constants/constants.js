export const JsonFormatterAPI = 'https://formatter-container-2b4cd56mpa-as.a.run.app/transform';

export const header = "Report Generator";

export function matrix(){
    var grid = [];
    for (let i=0; i<=50; i++) {
        var temp = []
        for (let j=0; j<=50; j++){
          temp[j] = { value:'', className:"x_"+i.toString()+"_y_"+j.toString()}
        }
        grid[i] = temp
      }
    return grid;
}
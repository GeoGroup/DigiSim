function varargout = DigiSim(varargin)
% DIGISIM MATLAB code for DigiSim.fig
%      DIGISIM, by itself, creates a new DIGISIM or raises the existing
%      singleton*.
%
%      H = DIGISIM returns the handle to a new DIGISIM or the handle to
%      the existing singleton*.
%
%      DIGISIM('CALLBACK',hObject,eventData,handles,...) calls the local
%      function named CALLBACK in DIGISIM.M with the given input arguments.
%
%      DIGISIM('Property','Value',...) creates a new DIGISIM or raises the
%      existing singleton*.  Starting from the left, property value pairs are
%      applied to the GUI before DigiSim_OpeningFcn gets called.  An
%      unrecognized property name or invalid value makes property application
%      stop.  All inputs are passed to DigiSim_OpeningFcn via varargin.
%
%      *See GUI Options on GUIDE's Tools menu.  Choose "GUI allows only one
%      instance to run (singleton)".
%
% See also: GUIDE, GUIDATA, GUIHANDLES

% Edit the above text to modify the response to help DigiSim

% Last Modified by GUIDE v2.5 17-Jan-2018 18:20:39

% Begin initialization code - DO NOT EDIT
gui_Singleton = 1;
gui_State = struct('gui_Name',       mfilename, ...
                   'gui_Singleton',  gui_Singleton, ...
                   'gui_OpeningFcn', @DigiSim_OpeningFcn, ...
                   'gui_OutputFcn',  @DigiSim_OutputFcn, ...
                   'gui_LayoutFcn',  [] , ...
                   'gui_Callback',   []);
if nargin && ischar(varargin{1})
    gui_State.gui_Callback = str2func(varargin{1});
end

if nargout
    [varargout{1:nargout}] = gui_mainfcn(gui_State, varargin{:});
else
    gui_mainfcn(gui_State, varargin{:});
end
% End initialization code - DO NOT EDIT


% --- Executes just before DigiSim is made visible.
% update
function DigiSim_OpeningFcn(hObject, eventdata, handles, varargin)
% This function has no output args, see OutputFcn.
% hObject    handle to figure
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
% varargin   command line arguments to DigiSim (see VARARGIN)

% Choose default command line output for DigiSim
handles.output = hObject;

axes(handles.axes1)
addpath subroutine
addpath resource
load data.mat
geom_plot(P);
P=[];
% I=imread('logofem2.jpg'); 
% image(I) ;
axis off;
axes(handles.axes2)
I=imread('logo.jpg'); 
imshow(I) ;
axis off;
% axes(handles.axes3)
% axis off;
% axes(handles.axes4)
% axis off;
% Update handles structure
guidata(hObject, handles);

% UIWAIT makes DigiSim wait for user response (see UIRESUME)
% uiwait(handles.figure1);


% --- Outputs from this function are returned to the command line.
function varargout = DigiSim_OutputFcn(hObject, eventdata, handles) 
% varargout  cell array for returning output args (see VARARGOUT);
% hObject    handle to figure
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Get default command line output from handles structure
varargout{1} = handles.output;


% --- Executes on mouse press over axes background.
function axes2_ButtonDownFcn(hObject, eventdata, handles)
% hObject    handle to axes2 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)



function edit1_Callback(hObject, eventdata, handles)
% hObject    handle to edit1 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: get(hObject,'String') returns contents of edit1 as text
%        str2double(get(hObject,'String')) returns contents of edit1 as a double


% --- Executes during object creation, after setting all properties.
function edit1_CreateFcn(hObject, eventdata, handles)
% hObject    handle to edit1 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end



function edit2_Callback(hObject, eventdata, handles)
% hObject    handle to edit2 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: get(hObject,'String') returns contents of edit2 as text
%        str2double(get(hObject,'String')) returns contents of edit2 as a double


% --- Executes during object creation, after setting all properties.
function edit2_CreateFcn(hObject, eventdata, handles)
% hObject    handle to edit2 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end



function edit3_Callback(hObject, eventdata, handles)
% hObject    handle to edit3 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: get(hObject,'String') returns contents of edit3 as text
%        str2double(get(hObject,'String')) returns contents of edit3 as a double


% --- Executes during object creation, after setting all properties.
function edit3_CreateFcn(hObject, eventdata, handles)
% hObject    handle to edit3 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end


% --- Executes on button press in pushbutton1.
function pushbutton1_Callback(hObject, eventdata, handles)
% hObject    handle to pushbutton1 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
% addpath subroutine
global FileName PathName I
[FileName,PathName] = uigetfile('*.jpg','Select the digital image file');
fn=[PathName,FileName];
I=imread(fn);
I=I(:,:,1);
I(I<200)=0;
I(I>200)=1;
axes(handles.axes3)
imshow(I*255);
I=1-I;






% --- Executes on button press in pushbutton2.
function pushbutton2_Callback(hObject, eventdata, handles)
% hObject    handle to pushbutton2 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
addpath subroutine
addpath resource
global FileName PathName P I
fn=[PathName,FileName];
error=str2double(get(handles.edit1,'String'));
scale=str2double(get(handles.edit2,'String'));
set(handles.pushbutton2,'String','Please Waiting');
pause(0.001);
disp(fn);
disp(size(I));
[P] = vectorization2(I,error);

P=geom_scale(P,scale);
% I=imread(fn);
axes(handles.axes4)
plot(nan,nan)
geom_plot(P);

set(handles.pushbutton2,'String','Finsh');
% imshow(I);


% --- Executes on button press in pushbutton3.
function pushbutton3_Callback(hObject, eventdata, handles)
% hObject    handle to pushbutton3 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
set(handles.pushbutton3,'String','Please Waiting');
pause(0.001);
global FileName PathName P
fn=[PathName,FileName(1:length(FileName)-4),'.xls'];
[parea,fraction]=geom_area(P);
mg=min_bound_box2(P);
mbr_plot(mg)
geom_stas(fn,parea,fraction,mg,P);
set(handles.pushbutton3,'String','Finsh');




function edit4_Callback(hObject, eventdata, handles)
% hObject    handle to edit4 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: get(hObject,'String') returns contents of edit4 as text
%        str2double(get(hObject,'String')) returns contents of edit4 as a double


% --- Executes during object creation, after setting all properties.
function edit4_CreateFcn(hObject, eventdata, handles)
% hObject    handle to edit4 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end



function edit5_Callback(hObject, eventdata, handles)
% hObject    handle to edit5 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: get(hObject,'String') returns contents of edit5 as text
%        str2double(get(hObject,'String')) returns contents of edit5 as a double


% --- Executes during object creation, after setting all properties.
function edit5_CreateFcn(hObject, eventdata, handles)
% hObject    handle to edit5 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end


% --- Executes on button press in pushbutton4.
function pushbutton4_Callback(hObject, eventdata, handles)
% hObject    handle to pushbutton4 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
set(handles.pushbutton4,'String','Please Waiting');
pause(0.001);
global FileName PathName P
dxf_file=[PathName,FileName(1:length(FileName)-4),'.dxf'];
dxf_file_write(P,dxf_file);
% disp('OK Dxf');
lc2=str2double(get(handles.edit3,'String'));
lc=str2double(get(handles.edit4,'String'));
radius=str2double(get(handles.edit5,'String'));
gmsh_file=[PathName,FileName(1:length(FileName)-4),'.geo'];
% lc=5;lc2=10;radius=1;
gmsh_file_write(P,gmsh_file,lc,lc2);
% disp('OK Gmsh');
abaqus_file=[PathName,FileName(1:length(FileName)-4),'.py'];
write_abaqus_2d(abaqus_file,P)
% disp('OK Abaqus');
pfc_file=[PathName,FileName(1:length(FileName)-4),'.p2dat'];
write_pfc_2d_group(P,radius,pfc_file);
% disp('OK PFC');
set(handles.pushbutton4,'String','Finsh');


% --- Executes on button press in pushbutton5.
function pushbutton5_Callback(hObject, eventdata, handles)
% hObject    handle to pushbutton5 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
close(handles.figure1);

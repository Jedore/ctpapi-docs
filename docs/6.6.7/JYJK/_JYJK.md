<table border="0" cellspacing="0" class="square-block" id=""><tbody border="0"><tr border="0"><td class="square-block-left"></td><td class="square-block-content"><div>

</div></td><td class="square-block-right"></td></tr></tbody></table>
<span class="anchor" id="0352366d-91d7-4e93-830f-b0fa447b6caf"></span>
## 1.说明
<p>交易员API提供了两个接口，分别为<a href="../CTHOSTFTDCTRADERSPI/_CTHOSTFTDCTRADERSPI/">CThostFtdcTraderApi</a>和<a href="../CTHOSTFTDCTRADERAPI/_CTHOSTFTDCTRADERAPI/">CThostFtdcTraderSpi</a>。这两个接口对FTD协议进行了封装，方便客户端应用程序的开发。客户端应用程序可以通过<a href="../CTHOSTFTDCTRADERSPI/_CTHOSTFTDCTRADERSPI/">CThostFtdcTraderApi</a>发出操作请求，通过继承<a href="../CTHOSTFTDCTRADERAPI/_CTHOSTFTDCTRADERAPI/">CThostFtdcTraderSpi</a>并重载回调函数来处理后台服务的响应。</p>
<p>交易员客户端应用程序至少由两个线程组成，一个是应用程序主线程，一个是交易员API工作线程。应用程序与交易系统的通讯是由 API工作线程驱动的。<a href="../CTHOSTFTDCTRADERSPI/_CTHOSTFTDCTRADERSPI/">CThostFtdcTraderApi</a>提供的接口是线程安全的，可以有多个应用程序线程同时发出请求。<a href="../CTHOSTFTDCTRADERAPI/_CTHOSTFTDCTRADERAPI/">CThostFtdcTraderSpi</a>提供的接口回调是由API工作线程驱动，通过实现SPI中的接口方法，可以从交易托管系统收取所需数据。</p>
<p>如果重载的某个回调函数阻塞，则等于阻塞了API工作线程，API与交易系统的通讯会停止。因此，在 <a href="../CTHOSTFTDCTRADERAPI/_CTHOSTFTDCTRADERAPI/">CThostFtdcTraderSpi</a> 派生类的回调函数中，通常应迅速返回，可以利用将数据放入缓冲区或通过Windows的消息机制来实现。</p>
<p>交易员 API 在运行过程中，会将一些数据写入本地文件中。调用<a href="../CTHOSTFTDCTRADERSPI/CREATEFTDCTRADERAPI/">CreateFtdcTraderApi</a>函数，可以传递一个参数，指明存贮本地文件的路径。该路径必须在运行前已创建好。本地文件的扩展名都是”.con”。</p>
<p>注意以下事项：</p>
<blockquote>
<p>init和release不是线程安全的，多线程使用需要加锁</p>
<p>在<a href="../CTHOSTFTDCTRADERAPI/_CTHOSTFTDCTRADERAPI/">CThostFtdcTraderSpi</a> 派生类的回调函数中应及时返回，不要阻塞。</p>
<p>API请求的输入参数不能为 NULL。 </p>
<p>API请求的返回参数，0表示正确，其他表示错误，详细错误编码请查error.xml。</p>
<p>API一个进程中linux最多开180-200左右的连接数，windows最多开400左右连接数，想建立更多连接请多开进程。</p>
<p>CTP系统支持的<a href="../../QTYWGZ/SJLSM/">通讯模式</a>有三种：对话<a href="../../QTYWGZ/SJLSM/">通讯模式</a>，私有<a href="../../QTYWGZ/SJLSM/">通讯模式</a>，广播<a href="../../QTYWGZ/SJLSM/">通讯模式</a>。详细说明见<a href="../../QTYWGZ/SJLSM/">[通讯模式]</a></p>
</blockquote>
<span class="anchor" id="2909bb30-0c90-4b0e-9eeb-18ac7b504a50"></span>
## 2.代码示例
<p>下面通过一个简单的代码示例，带大家快速了解下交易API的使用方法。该示例演示了API的初始化、订阅私有流、连接前置、登录交易系统、报单和查询等过程。</p>
<span class="anchor" id="dc92a671-9125-4577-87e3-a939d5bf6653"></span>
### 2.1.源代码
<pre><code>01.     //以下是tradehandler.h文件
02.     
03.     #include "ThostFtdcTraderApi.h"
04.     
05.     #include "traderApi.h"
06.     
07.     #include &lt;string.h&gt;
08.     
09.     #include &lt;stdio.h&gt;
10.     
11.     #include &lt;Windows.h&gt;
12.     
13.      
14.     
15.     class CTraderHandler : public CThostFtdcTraderSpi
16.     
17.     {
18.     
19.     private:
20.     
21.       CThostFtdcTraderApi *m_ptraderapi;
22.     
23.      
24.     
25.     public:
26.     
27.       void connect()
28.     
29.       {
30.     
31.           //创建API实例
32.     
33.           m_ptraderapi = CThostFtdcTraderApi::CreateFtdcTraderApi(".//flow/"); //必须提前创建好flow目录，流文件*.con就会在该文件夹下面创建，如果想要区别不同session创建的流水文件名称可见如下示例“.//flow/a_”
34.     
35.           m_ptraderapi-&gt;RegisterSpi(this);
36.     
37.           m_ptraderapi-&gt;SubscribePublicTopic(THOST_TERT_QUICK);
38.     
39.           m_ptraderapi-&gt;SubscribePrivateTopic(THOST_TERT_QUICK); //设置私有流订阅模式
40.     
41.           m_ptraderapi-&gt;RegisterFront("tcp://127.0.0.1:41205");
42.     
43.           m_ptraderapi-&gt;Init();
44.     
45.           //输出API版本信息
46.     
47.           printf("%s\n", m_ptraderapi-&gt;GetApiVersion());
48.     
49.       }
50.     
51.      
52.     
53.       //释放
54.     
55.       void release()
56.     
57.       {
58.     
59.           m_ptraderapi-&gt;Release();
60.     
61.       }
62.     
63.      
64.     
65.       //登陆
66.     
67.       void login()
68.     
69.       {
70.     
71.           CThostFtdcReqUserLoginField t = {0};
72.     
73.           strcpy_s(t.BrokerID, "1701");
74.     
75.           strcpy_s(t.UserID, "1701_admin");
76.     
77.           strcpy_s(t.Password, "1701_admin");
78.     
79.           while (m_ptraderapi-&gt;ReqUserLogin(&amp;t, 1)!=0)   Sleep(1000);
80.     
81.       }
82.     
83.      
84.     
85.       //结算单确认
86.     
87.       void settlementinfoConfirm()
88.     
89.       {
90.     
91.           CThostFtdcSettlementInfoConfirmField t = {0};
92.     
93.           strcpy_s(t.BrokerID, "1701");
94.     
95.           strcpy_s(t.InvestorID, "00001");
96.     
97.           while (m_ptraderapi-&gt;ReqSettlementInfoConfirm(&amp;t, 2)!=0)  Sleep(1000);
98.     
99.       }
100.        
101.         
102.        
103.          //报单
104.        
105.          void orderinsert()
106.        
107.          {
108.        
109.              CThostFtdcInputOrderField t = { 0 };
110.        
111.              strcpy_s(t.BrokerID, "9999");
112.        
113.              strcpy_s(t.InvestorID, "00001");
114.        
115.              strcpy_s(t.UserID, "00001");
116.        
117.              t.Direction = THOST_FTDC_D_Buy;
118.        
119.              t.CombOffsetFlag[0] = THOST_FTDC_OF_Open;
120.        
121.              t.CombHedgeFlag[0] = THOST_FTDC_HF_Speculation;
122.        
123.              t.ContingentCondition = THOST_FTDC_CC_Immediately;
124.    
125.              strcpy_s(t.InstrumentID, "sc1807");
126.        
127.              t.ForceCloseReason = THOST_FTDC_FCC_NotForceClose;
128.        
129.              t.LimitPrice = 490;
130.        
131.              t.OrderPriceType = THOST_FTDC_OPT_LimitPrice;
132.        
133.              t.VolumeCondition = THOST_FTDC_VC_AV;
134.        
135.              t.TimeCondition = THOST_FTDC_TC_GFD;
136.        
137.              t.VolumeTotalOriginal = 1;
138.        
139.              strcpy_s(t.OrderRef, "0000001");
140.    
141.              strcpy_s(t.ExchangeID, "INE");
142.        
143.              while (m_ptraderapi-&gt;ReqOrderInsert(&amp;t, 3) != 0) Sleep(1000);
144.        
145.          }
146.        
147.          //查询合约
148.        
149.          void qryInstrument()
150.        
151.          {
152.        
153.              CThostFtdcQryInstrumentField t = { 0 };
154.        
155.              strcpy_s(t.ExchangeID, "SHFE");
156.        
157.              strcpy_s(t.InstrumentID, "zn1803");
158.        
159.              while (m_ptraderapi-&gt;ReqQryInstrument(&amp;t, 4) != 0) Sleep(1000);
160.        
161.          }
162.        
163.         
164.        
165.        //前置连接响应
166.        
167.          void OnFrontConnected()
168.        
169.          {
170.        
171.              printf("OnFrontConnected\n");
172.        
173.          }
174.        
175.         
176.        
177.          //登陆请求响应
178.        
179.          void OnRspUserLogin(CThostFtdcRspUserLoginField *pRspUserLogin, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
180.        
181.          {
182.        
183.              printf("OnRspUserLogin\n");
184.        
185.          }
186.        
187.         
188.        
189.          //结算单确认响应
190.        
191.          void OnRspSettlementInfoConfirm(CThostFtdcSettlementInfoConfirmField *pSettlementInfoConfirm, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
192.        
193.          {
194.        
195.              printf("OnRspSettlementInfoConfirm\n");
196.        
197.          }
198.        
199.         
200.        
201.          //查询合约响应
202.        
203.          void OnRspQryInstrument(CThostFtdcInstrumentField *pInstrument, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
204.        
205.          {
206.        
207.              printf("OnRspQryInstrument\n");
208.        
209.          }
210.         
211.        
212.          //报单通知
213.        
214.          void OnRtnOrder(CThostFtdcOrderField *pOrder)
215.        
216.          {
217.        
218.              printf("OnRtnOrder\n");
219.        
220.          }
221.        
222.          
223.        
224.          //成交通知
225.        
226.          void OnRtnTrade(CThostFtdcTradeField *pTrade)
227.        
228.          {
229.        
230.              printf("OnRtnTrade\n");
231.        
232.          }
233.        
234.         
235.        
236.          //报单录入请求响应
237.        
238.          void OnRspOrderInsert(CThostFtdcInputOrderField *pInputOrder, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
239.        
240.          {
241.        
242.              printf("OnRspOrderInsert\n");
243.        
244.          }
245.        
246.          
247.        
248.          //错误应答
249.        
250.          void OnRspError(CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
251.        
252.          {
253.        
254.              printf("OnRspError\n");
255.        
256.          }
257.        
258.        };
259.        
260.        //以下是main.cpp文件 
261.        
262.        #include "tradehandler.h"
263.        
264.        int main(int argc, char *argv[])
265.        
266.        {
267.        
268.          CTraderHandler *trader = new CTraderHandler();
269.        
270.          trader-&gt;connect();
271.        
272.          Sleep(2000);
273.        
274.          trader-&gt;login();
275.        
276.          Sleep(2000);
277.        
278.          trader-&gt;settlementinfoConfirm();
279.        
280.          Sleep(2000);
281.        
282.          trader-&gt;qryInstrument();
283.        
284.          Sleep(2000);
285.        
286.          trader-&gt;orderinsert();
287.        
288.          Sleep(INFINITE);
289.    
290.          trader-&gt;release();
291.        
292.          return 1;
293.        
294.        }
</code></pre>
<span class="anchor" id="bd42d4a9-ddd9-48ad-91d7-85f618ff39c8"></span>
### 2.2.代码说明
<span class="anchor" id="3637d5f1-97ca-4a97-a8d0-2161691cd47a"></span>
#### 2.2.1.继承CThostFtdcTraderSpi类
<p>代码一开始通过<code>#include "ThostFtdcTraderApi.h"</code>，将thosttraderapi.lib中声明的类和数据类型包括进来，该头文件中有两个重要的基类：<a href="../CTHOSTFTDCTRADERAPI/_CTHOSTFTDCTRADERAPI/">CThostFtdcTraderSpi</a>和<a href="../CTHOSTFTDCTRADERSPI/_CTHOSTFTDCTRADERSPI/">CThostFtdcTraderApi</a>。</p>
<p><a href="../CTHOSTFTDCTRADERAPI/_CTHOSTFTDCTRADERAPI/">CThostFtdcTraderSpi</a>类提供了交易相关的回调接口，用户需要继承该类并重载这些接口，以获取响应数据。</p>
<p><a href="../CTHOSTFTDCTRADERSPI/_CTHOSTFTDCTRADERSPI/">CThostFtdcTraderApi</a>类则是提供了交易相关功能的请求接口，例如查询请求、报单请求、报价请求等。</p>
<p>第15行我们声明了一个CTraderHandler类，该类正是继承了<a href="../CTHOSTFTDCTRADERAPI/_CTHOSTFTDCTRADERAPI/">CThostFtdcTraderSpi</a>类，并且重载了<a href="../CTHOSTFTDCTRADERAPI/ONFRONTCONNECTED/">OnFrontConnected</a>、<a href="../../HQJK/CTHOSTFTDCMDSPI/ONRSPUSERLOGIN/">OnRspUserLogin</a>、<a href="../../HQJK/CTHOSTFTDCMDSPI/ONRSPERROR/">OnRspError</a>、<a href="../CTHOSTFTDCTRADERAPI/ONRSPORDERINSERT/">OnRspOrderInsert</a>等接口。通过这种方式，例如当我们API和前置建立连接时，便会触发<a href="../CTHOSTFTDCTRADERAPI/ONFRONTCONNECTED/">OnFrontConnected</a>；当我们发起登录请求后，便会触发<a href="../../HQJK/CTHOSTFTDCMDSPI/ONRSPUSERLOGIN/">OnRspUserLogin</a>。通过这些回调返回的数据，我们可以得知当前业务处理的结果或者获取我们想要的业务数据，进一步实现自己的业务逻辑。</p>
<p>第21行，声明了一个<a href="../CTHOSTFTDCTRADERSPI/_CTHOSTFTDCTRADERSPI/">CThostFtdcTraderApi</a>类型的变量m_ptraderapi，后续我们会实例化它，以便我们使用tradeapi提供的登录、报单和查询等功能。</p>
<span class="anchor" id="9366f16e-eb37-463a-ab03-e6772562fb6d"></span>
#### 2.2.2.初始化
<p>第27行到43行<code>connect()</code>函数里，实现了线程的初始化，步骤为：</p>
<p class="step-para"><span class="step-mark">Step 1</span> 创建Api实例（<a href="../CTHOSTFTDCTRADERSPI/CREATEFTDCTRADERAPI/">CreateFtdcTraderApi</a>）并为其注册对应的回调接口类的实例（<a href="../../HQJK/CTHOSTFTDCMDAPI/REGISTERSPI/">RegisterSpi</a>）。</p>
<p class="step-para"><span class="step-mark">Step 2</span> 订阅私有流（<a href="../CTHOSTFTDCTRADERSPI/SUBSCRIBEPRIVATETOPIC/">SubscribePrivateTopic</a>）。</p>
<p class="step-para"><span class="step-mark">Step 3</span> 订阅公有流（<a href="../CTHOSTFTDCTRADERSPI/SUBSCRIBEPUBLICTOPIC/">SubscribePublicTopic</a>）。</p>
<p class="step-para"><span class="step-mark">Step 4</span> 注册名称服务器网络地址（<a href="../CTHOSTFTDCTRADERSPI/REGISTERNAMESERVER/">RegisterNameServer</a>）或注册前置机网络地址（<a href="../../HQJK/CTHOSTFTDCMDAPI/REGISTERFRONT/">RegisterFront</a>）。</p>
<p class="step-para"><span class="step-mark">Step 5</span> 初始化Api（<a href="../../HQJK/CTHOSTFTDCMDAPI/INIT/">Init</a>），使API建立与前置的连接，连接成功后回调<a href="../CTHOSTFTDCTRADERAPI/ONFRONTCONNECTED/">OnFrontConnected</a>。</p>
<p>第33行创建了一个api实例，并将其赋值给m_ptraderapi，同时参数<code>".//flow/"</code>指明我们api流水文件存放的目录为flow目录，因此在运行程序前，我们需要手工创建好这个目录！</p>
<blockquote>
<p>流水文件以.con文件类型方式存放流水序号和交易日信息，这些信息对api正常工作有重要意义，不可随意修改和删除！并且多个api实例不可共享一个流水文件，必须通过不同文件夹或者不同流水文件名区分开。</p>
</blockquote>
<p>第35行将自己定义的继承了Spi类的CTraderHandler注册给<a href="../CTHOSTFTDCTRADERSPI/_CTHOSTFTDCTRADERSPI/">CThostFtdcTraderApi</a>，这样API就能将收到的各种数据通过Spi类的接口回调给用户。</p>
<p>第37行使用QUICK模式订阅了私有流。订阅私有流的方式有很多种，可以参见<a href="../CTHOSTFTDCTRADERSPI/SUBSCRIBEPRIVATETOPIC/">SubscribePrivateTopic</a>的接口说明。</p>
<p>第41行注册了前置地址，如果有多个地址，可以多次调用<a href="../../HQJK/CTHOSTFTDCMDAPI/REGISTERFRONT/">RegisterFront</a>函数传入不同的地址来实现。</p>
<p>第43行调用<a href="../../HQJK/CTHOSTFTDCMDAPI/INIT/">Init</a>()函数开始正式初始化api，也就是说前面的工作只是准备工作，到了这里api才真正开始工作。此时api会按照之前设置的私有流订阅方式和注册的地址发起与CTP前置的连接。</p>
<blockquote>
<p>init和release不是线程安全的，多线程使用需要加锁。</p>
</blockquote>
<p>完成以上步骤后，客户端就已经和ctp的交易前置建立了连接。</p>
<p>第167行到173行，如果成功建立连接，<a href="../CTHOSTFTDCTRADERAPI/ONFRONTCONNECTED/">OnFrontConnected</a>就会被调用。后续我们就可以调用各种API接口完成业务需求。</p>
<span class="anchor" id="ea481f79-64b4-4946-a135-1400af78b45f"></span>
#### 2.2.3.显示api版本号
<p>第47行，打印当前api的版本号。</p>
<span class="anchor" id="53dccdf7-d9f5-42d1-9e1f-026394bddca3"></span>
#### 2.2.4.释放api线程
<p>第55行到61行，释放了api线程，释放后api资源会被回收，并且与前置断开连接。</p>
<span class="anchor" id="d2af1d06-7222-4b6b-b959-f14a5bf8be87"></span>
#### 2.2.5.登录
<p>第67到81行，前置连接成功后能够开始登陆交易系统了，先初始化登陆结构体，再赋值相应字段。brokerid、userid、password都是必要字段。之后发送登陆（<a href="../../HQJK/CTHOSTFTDCMDAPI/REQUSERLOGIN/">ReqUserLogin</a>）指令。通过返回值可以判断是否发送成功，0表示成功，其他则表示失败，具体可以参考接口<a href="../CTHOSTFTDCTRADERSPI/REQUSERLOGIN/">ReqUserLogin</a>。发送不成功可以尝试等待一小会重发。</p>
<blockquote>
<p>注意这里返回0不表示登录成功，而是仅仅表示api指令发出去了。该规则同样适用于其他请求接口，建议在实际应用中做好超时重发机制，以便在网络丢包的情况下能够及时重发指令。</p>
</blockquote>
<p>在响应里，FrontID和SessionID是非常重要的两个ID，他标识了本次登录的当天唯一编号。对于api用户来说，如果同一用户有多个同时在线的会话，鉴于api的私有流机制，他们彼此间可以互收私有流（例如0001投资者，session1报单，session2也能收到回报），此时就可以用这组ID来过滤非本会话的私有流数据，因为对于不同的会话，这组ID是不同的；而对于交易系统来说，则可以用来定位客户的各种交易行为。</p>
<p>第179到185行，为请求登录后的响应。</p>
<span class="anchor" id="83a16777-8ec9-4c83-aec2-dc3fa42b7de5"></span>
#### 2.2.6.结算单确认
<p>第87到99行，每一个交易日第一次登陆都需要先确认结算，不然只能做查询，不能执行报单等交易请求。</p>
<p>第191到197行，为请求确认结算单后的响应。</p>
<span class="anchor" id="9fa9a5f3-bf63-4e66-b1b4-821c8a8619ea"></span>
#### 2.2.7.报单
<p>第105到143行，报入一笔限价立即单，报单属性为，多头，开仓，投机，立即单，合约为sc1807，非强平单，限价单价格为490，任意数量，当天有效，手数为1，报单引用OrderRef为"0000001",交易所为原油交易所。</p>
<blockquote>
<p>注意，报单引用（OrderRef）是同一个sessionid下必须唯一且递增的一个值，不要求连续递增，但是必须要递增。而且，必须是数字，不能有英文字母！</p>
</blockquote>
<p>第238到244行，如果报单填错了字段，或者客户资金不足，则报单指令发出后会被CTP拒绝，触发<a href="../CTHOSTFTDCTRADERAPI/ONRSPORDERINSERT/">OnRspOrderInsert</a>回调，返回"CTP：..."这类的报错。</p>
<p>第214到220行，报单请求通过交易核心的合法性验证后，通过<a href="../CTHOSTFTDCTRADERAPI/ONRTNORDER/">OnRtnOrder</a>返回。一开始会返回未知单，之后会实时推送更新的报单状态。</p>
<p>第226到232行，报单成交后响应，通过<a href="../CTHOSTFTDCTRADERAPI/ONRTNTRADE/">OnRtnTrade</a>返回。</p>
<span class="anchor" id="fa8b435e-c9c0-468f-b717-9d0424b90074"></span>
#### 2.2.8.查询合约
<p>第149到161行，请求查询合约信息。对于大部分查询接口，如果请求信息填空，则会返回所有的记录；但是也有例外，比如保证金率和手续费率，C必须指定合约，可以参考对应的接口说明。</p>
<p>第203到209行，请求查询合约后的响应。</p>
<span class="anchor" id="ecf08797-70ba-4054-b8d3-bd2b76f29eb1"></span>
#### 2.2.9.错误应答
<p>第250到256，错误应答返回。一些特殊的报错会通过该接口返回，例如错将行情端口当成交易端口，则会报无此功能，或者为没有权限的投资者报单会报无此权限，等等。</p>
<span class="anchor" id="dad2cdff-f6e6-4bb9-a469-174e0eb04c55"></span>
#### 2.2.10.程序运行流程
<p>第264到292行，首先初始化CTraderHandler类。调用connect函数开始连接ctp前置，依次执行登录，结算单确认，查询合约，报单操作。</p>
<div class="sub-links-list" style="text-indent:0px;"><hr class="SubLinksListLine"/>
<p class="sub-links-list-header">请参阅：</p>
<p class="sub-links-paragraph"> &gt;&gt; <a class="sub-links-action" href="../CTHOSTFTDCTRADERAPI/_CTHOSTFTDCTRADERAPI/">CThostFtdcTraderSpi</a></p>
<p class="sub-links-paragraph"> &gt;&gt; <a class="sub-links-action" href="../CTHOSTFTDCTRADERSPI/_CTHOSTFTDCTRADERSPI/">CThostFtdcTraderApi</a></p>
</div>

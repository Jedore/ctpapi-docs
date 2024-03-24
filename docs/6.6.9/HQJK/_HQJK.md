<table border="0" cellspacing="0" class="square-block" id=""><tbody border="0"><tr border="0"><td class="square-block-left"></td><td class="square-block-content"><div>

</div></td><td class="square-block-right"></td></tr></tbody></table>
<span class="anchor" id="07ecdab3-1299-47c5-b607-6e95120ee44d"></span>
## 1.说明
<p>行情API提供了两个接口，分别为<a href="../CTHOSTFTDCMDAPI/_CTHOSTFTDCMDAPI/">CThostFtdcMdApi</a>和<a href="../CTHOSTFTDCMDSPI/_CTHOSTFTDCMDSPI/">CThostFtdcMdSpi</a>。这两个接口对FTD协议进行了封装，方便客户端应用程序的开发。客户端应用程序可以通过<a href="../CTHOSTFTDCMDAPI/_CTHOSTFTDCMDAPI/">CThostFtdcMdApi</a>发出操作请求，通过继承<a href="../CTHOSTFTDCMDSPI/_CTHOSTFTDCMDSPI/">CThostFtdcMdSpi</a>并重载回调函数来处理后台服务的响应。</p>
<blockquote>
<p><code>特别注意</code>：CTP系统在早盘系统启动时，会重演夜盘流水，此时有可能重复推送整个夜盘的行情。如果用户此时连入CTP就有可能收到这些重复行情，因此建议用户在处理行情时过滤掉重复行情，以免影响程序逻辑。</p>
<p>自6.6.2P8柜台版本开始front<em>md</em>se行情前置带流重启后，不再推送夜盘行情数据。</p>
</blockquote>
<span class="anchor" id="0b5ce1b2-cd93-49c0-ac36-ef39bdbe8f60"></span>
## 2.代码示例
<span class="anchor" id="70a0f101-b107-4884-9483-4dee43afe583"></span>
### 2.1.源代码
<p>下面通过一个简单的代码示例，带大家快速了解下行情API的使用方法。该示例演示了API的初始化、连接前置、登录行情系统和订阅行情的过程。</p>
<pre><code>01. //以下是mduserhandle.h文件
02. 
03. #include "ThostFtdcMdApi.h"
04. 
05. #include &lt;stdio.h&gt;
06. 
07. #include &lt;Windows.h&gt;
08. 
09.  
10. 
11. class CMduserHandler : public CThostFtdcMdSpi
12. 
13. {
14. 
15. private:
16. 
17.   CThostFtdcMdApi *m_mdApi;
18. 
19.  
20. 
21. public:
22. 
23.   void connect()
24. 
25.   {
26. 
27. //创建并初始化API
28. 
29.       m_mdApi = CThostFtdcMdApi::CreateFtdcMdApi(".//flow_md/", true, true);
30. 
31.       m_mdApi-&gt;RegisterSpi(this);
32. 
33.       m_mdApi-&gt;RegisterFront("tcp://218.28.130.102:41413");
34. 
35.       m_mdApi-&gt;Init();
36. 
37.   }
38. 
39.  
40. 
41. //登陆
42. 
43.   void login()
44. 
45.   {
46. 
47.       CThostFtdcReqUserLoginField t = {0};
48. 
49.       while (m_mdApi-&gt;ReqUserLogin(&amp;t, 1)!=0) Sleep(1000);
50. 
51.   }
52. 
53.  
54. 
55. // 订阅行情
56. 
57.   void subscribe()
58. 
59.   {
60. 
61.       char **ppInstrument=new char * [50];
62. 
63.       ppInstrument[0] = "IF1809";
64. 
65.       while (m_mdApi-&gt;SubscribeMarketData(ppInstrument, 1)!=0) Sleep(1000);
66. 
67.   }
68. 
69.  
70. 
71.   //接收行情
72. 
73.   void OnRtnDepthMarketData(CThostFtdcDepthMarketDataField *pDepthMarketData)
74. 
75.   {
76. 
77.           printf("OnRtnDepthMarketData\n");
78. 
79.   }
80. 
81. };
82. 
83.  
84. 
85. // 以下是main.cpp文件
86. 
87. #include "mduserhandle.h"
88. 
89. int main(int argc, char* argv[])
90. 
91. {
92. 
93.   CMduserHandler *mduser = new CMduserHandler;
94. 
95.   mduser-&gt;connect();
96. 
97.   mduser-&gt;login();
98. 
99.   mduser-&gt;subscribe();
100.    
101.  Sleep(INFINITE);
102.    
103. }
</code></pre>
<span class="anchor" id="cf0617d4-2f52-4079-b44f-390702d8e054"></span>
### 2.2.代码说明
<span class="anchor" id="be60e5cb-777e-4a33-b013-9996a94d67c7"></span>
#### 2.2.1.继承CThostFtdcMdSpi类
<p>代码一开始通过<code>#include "ThostFtdcMdApi.h"</code>，将thostmduserapi.lib中声明的类和数据类型包括进来，该头文件中有两个重要的基类：<a href="../CTHOSTFTDCMDSPI/_CTHOSTFTDCMDSPI/">CThostFtdcMdSpi</a>和<a href="../CTHOSTFTDCMDAPI/_CTHOSTFTDCMDAPI/">CThostFtdcMdApi</a>。</p>
<p><a href="../CTHOSTFTDCMDSPI/_CTHOSTFTDCMDSPI/">CThostFtdcMdSpi</a>类提供了行情相关的回调接口，用户需要继承该类并重载这些接口，以获取响应数据。</p>
<p><a href="../CTHOSTFTDCMDAPI/_CTHOSTFTDCMDAPI/">CThostFtdcMdApi</a>类则是提供了行情相关的请求接口，例如订阅行情请求、订阅询价请求。</p>
<p>第11行我们声明了一个CMduserHandler类，该类正是继承了<a href="../CTHOSTFTDCMDSPI/_CTHOSTFTDCMDSPI/">CThostFtdcMdSpi</a>类，并且重载了<a href="../CTHOSTFTDCMDSPI/ONRTNDEPTHMARKETDATA/">OnRtnDepthMarketData</a>等接口。通过这种方式，例如当我们API和前置建立连接成功时，便会触发<a href="../../JYJK/CTHOSTFTDCTRADERAPI/ONFRONTCONNECTED/">OnFrontConnected</a>；当我们发起订阅行情请求成功后，便会触发<a href="../CTHOSTFTDCMDSPI/ONRSPSUBMARKETDATA/">OnRspSubMarketData</a>。通过这些回调返回的数据，我们可以得知订阅是否成功，之后交易系统会通过<a href="../CTHOSTFTDCMDSPI/ONRTNDEPTHMARKETDATA/">OnRtnDepthMarketData</a>实时推送行情。</p>
<p>第17行，声明了一个<a href="../CTHOSTFTDCMDAPI/_CTHOSTFTDCMDAPI/">CThostFtdcMdApi</a>类型的变量m_mdApi，后续我们会实例化它，创建实例后便可以调用mdapi提供的登录，订阅行情等接口功能。</p>
<span class="anchor" id="78b6614c-0e34-4771-b3fc-1476e492e703"></span>
#### 2.2.2.初始化
<p>第23行到37行<code>connect()</code>函数里，实现了线程的初始化，步骤为：</p>
<p class="step-para"><span class="step-mark">Step 1</span> 创建Api实例（<a href="../CTHOSTFTDCMDAPI/_CTHOSTFTDCMDAPI/">CThostFtdcMdApi</a>）并为其注册对应的回调接口类的实例（<a href="../../JYJK/CTHOSTFTDCTRADERSPI/REGISTERSPI/">RegisterSpi</a>）。</p>
<p class="step-para"><span class="step-mark">Step 2</span> 注册名称服务器网络地址（<a href="../CTHOSTFTDCMDAPI/REGISTERNAMESERVER/">RegisterNameServer</a>）或注册前置机网络地址（<a href="../../JYJK/CTHOSTFTDCTRADERSPI/REGISTERFRONT/">RegisterFront</a>）。</p>
<p class="step-para"><span class="step-mark">Step 3</span> 初始化Api（<a href="../CTHOSTFTDCMDAPI/INIT/">Init</a>），使API建立与前置的连接，连接成功后回调<a href="../../JYJK/CTHOSTFTDCTRADERAPI/ONFRONTCONNECTED/">OnFrontConnected</a>。</p>
<p>第29行创建了一个api实例，并将其赋值给m_mdApi，同时参数<code>".//flow_md/"</code>指明我们api流水文件存放的目录为flow目录，因此在运行程序前，我们需要手工创建好这个目录！</p>
<blockquote>
<p>流水文件以.con文件类型方式存放流水序号和交易日信息，这些信息对api正常工作有重要意义，不可随意修改和删除！并且多个api实例不可共享一个流水文件，必须通过不同文件夹或者不同流水文件名区分开。虽然行情没有私有流，但是也建议遵循以上规则。</p>
</blockquote>
<p>第31行将自己定义的继承了Spi类的CMduserHandler注册给<a href="../CTHOSTFTDCMDAPI/_CTHOSTFTDCMDAPI/">CThostFtdcMdApi</a>，这样API就能将收到的各种数据通过Spi类的接口回调给用户。</p>
<p>第33行注册了前置地址，如果有多个地址，可以多次调用<a href="../../JYJK/CTHOSTFTDCTRADERSPI/REGISTERFRONT/">RegisterFront</a>函数传入不同的地址来实现。API会择优挑选一个地址进行连接。</p>
<p>第35行调用<a href="../CTHOSTFTDCMDAPI/INIT/">Init</a>()函数开始正式初始化api，也就是说前面的工作只是准备工作，到了这里api才真正开始工作。此时api会向之前注册的地址发起与CTP前置的连接。</p>
<p>完成以上步骤后，客户端就已经和ctp的行情前置建立了连接，后续我们就可以调用各种API接口完成业务需求。</p>
<span class="anchor" id="338496d9-7ae1-45d8-a6e7-77b8df4e40d1"></span>
#### 2.2.3.登录
<p>第43到51行，前置连接成功后能够开始登陆交易系统了，先初始化登陆结构体，再赋值相应字段。对于行情的登录来说只需要调用登录接口即可，目前CTP暂时不对行情做密码校验。之后发送登陆（<a href="../CTHOSTFTDCMDAPI/REQUSERLOGIN/">ReqUserLogin</a>）指令。通过返回值可以判断是否发送成功，0表示成功，其他则表示失败，具体可以参考接口<a href="../CTHOSTFTDCMDAPI/REQUSERLOGIN/">ReqUserLogin</a>。发送不成功可以尝试等待一小会重发。</p>
<blockquote>
<p>注意这里返回0不表示登录成功，而是仅仅表示api指令发出去了。该规则同样适用于其他请求接口，建议在实际应用中做好超时重发机制，以便在网络丢包的情况下能够及时重发指令。</p>
</blockquote>
<span class="anchor" id="4e15c061-1bb1-4117-bd21-7ee3b9eaf9fc"></span>
#### 2.2.4.订阅行情
<p>第57到67行，调用订阅行情的接口，我们这里订阅了合约<code>"IF1809"</code>。若需要批量订阅多个合约，则需要循环把合约输入到ppInstrumentID中去，同时别忘了更改合约数量（第二个参数）。订阅发出后通过<a href="../CTHOSTFTDCMDSPI/ONRSPSUBMARKETDATA/">OnRspSubMarketData</a>响应判断是否订阅成功。</p>
<p>第73到81行，订阅行情后，通过<a href="../CTHOSTFTDCMDSPI/ONRTNDEPTHMARKETDATA/">OnRtnDepthMarketData</a>回调推送实时行情信息。可以在此时实现自身业务逻辑。</p>
<blockquote>
<p>但是如果业务逻辑比较耗时，应该在另外一个线程处理，而不应该卡在此回调里，否则会导致后续的行情堵塞在API内部，严重情况下会导致断线。</p>
</blockquote>
<span class="anchor" id="6b9b00df-5367-4ca8-a8f2-ae1e05776133"></span>
#### 2.2.5.程序运行流程
<p>第89到103行，是我们的主函数，该函数是业务实现主体。首先初始化CMduserHandler类。调用connect函数开始连接ctp前置，然后依次执行登录和订阅行情操作。</p>
<div class="sub-links-list" style="text-indent:0px;"><hr class="SubLinksListLine"/>
<p class="sub-links-list-header">请参阅：</p>
<p class="sub-links-paragraph"> &gt;&gt; <a class="sub-links-action" href="../CTHOSTFTDCMDAPI/_CTHOSTFTDCMDAPI/">CThostFtdcMdApi</a></p>
<p class="sub-links-paragraph"> &gt;&gt; <a class="sub-links-action" href="../CTHOSTFTDCMDSPI/_CTHOSTFTDCMDSPI/">CThostFtdcMdSpi</a></p>
</div>

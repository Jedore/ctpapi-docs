<p>创建TraderApi实例。如果创建多个api实例，则每个实例的flow目录都要区分开，否则可能会导致报单回报丢失。</p>
<span class="anchor" id="19c63d32-0ed2-4fc8-9af5-74a571b7da26"></span>
## 1.函数原型
<p>static <a href="../_CTHOSTFTDCTRADERSPI/">CThostFtdcTraderApi</a> *CreateFtdcTraderApi(const char *pszFlowPath = "");</p>
<span class="anchor" id="9a3389ce-45d8-41ef-8e5a-06747afcb0dd"></span>
## 2.参数
<p>pszFlowPath：常量字符指针，用于指定一个文件目录来存贮交易托管系统发布消息的状态。默认值代表当前目录。</p>
<span class="anchor" id="ef946152-22d1-459f-965d-3069d0a91b23"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="8b0eac97-a3f2-4562-b65a-f2840960d07a"></span>
## 4.调用示例
<pre><code>//初始化api
CThostFtdcTraderApi *pUserApi = CThostFtdcTraderApi::CreateFtdcTraderApi("flow\\01\\");
CSimpleHandler sh(pUserApi);
pUserApi-&gt;RegisterSpi(&amp;sh);
pUserApi-&gt;SubscribePrivateTopic(THOST_TERT_QUICK);
pUserApi-&gt;SubscribePublicTopic(THOST_TERT_QUICK);
pUserApi-&gt;RegisterFront("tcp://127.0.0.1:41205");
pUserApi-&gt;Init();
//创建第二个api实例，要区分开flow目录
CThostFtdcTraderApi *pUserApi2 = CThostFtdcTraderApi::CreateFtdcTraderApi("flow\\02\\");
</code></pre>
<span class="anchor" id="fbbf34f1-35a6-4411-882b-62e8e3666008"></span>
## 5.FAQ
<p><div class="region_i"><p class="region_header" id="region_header_1" style="padding-left: 1em;font-weight : bold;text-indent: 0px;text-align: left;">“RuntimeError:can not open CFlow file in line 279 of file ....\source\userapi\ThostFtdcUserApiImplBase.cpp” 报错是什么意思？</p><div class="region_panel" id="region_panel_1" style="display:block;"><table><tr><td>
<p>程序运行之前，flow目录必须提前创建好，否则会报错。</p>
</td></tr></table>
</div><p class="region_tail" id="region_tail_1" style="border-top-color:transparent;border-bottom-width:0;"></p></div></p>

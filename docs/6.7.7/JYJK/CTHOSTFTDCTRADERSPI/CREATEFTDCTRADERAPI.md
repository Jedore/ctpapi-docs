<p>创建TraderApi实例。如果创建多个api实例，则每个实例的flow目录都要区分开，否则可能会导致报单回报丢失。</p>
<span class="anchor" id="01abdc50-fa03-486a-811b-1448d0084751"></span>
## 1.函数原型
<p>static <a href="../_CTHOSTFTDCTRADERSPI/">CThostFtdcTraderApi</a> *CreateFtdcTraderApi(const char *pszFlowPath = "");</p>
<span class="anchor" id="be5a9e72-1f49-4c84-a6c5-a0c396018e85"></span>
## 2.参数
<p>pszFlowPath：常量字符指针，用于指定一个文件目录来存贮交易托管系统发布消息的状态。默认值代表当前目录。</p>
<span class="anchor" id="ece4d94f-9431-41cc-a55a-f0462ebe3156"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="16e6211a-f1e9-4250-82f0-36166a537e27"></span>
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
<span class="anchor" id="009e40af-841f-44a6-a898-e0b715bef91e"></span>
## 5.FAQ
<p><div class="region_i"><p class="region_header" id="region_header_1" style="padding-left: 1em;font-weight : bold;text-indent: 0px;text-align: left;">“RuntimeError:can not open CFlow file in line 279 of file ....\source\userapi\ThostFtdcUserApiImplBase.cpp” 报错是什么意思？</p><div class="region_panel" id="region_panel_1" style="display:block;"><table><tr><td>
<p>程序运行之前，flow目录必须提前创建好，否则会报错。</p>
</td></tr></table>
</div><p class="region_tail" id="region_tail_1" style="border-top-color:transparent;border-bottom-width:0;"></p></div></p>
<p><span alt="" id="anchor-id-01"></span> </p>
<p><div class="region_i"><p class="region_header" id="region_header_2" style="padding-left: 1em;font-weight : bold;text-indent: 0px;text-align: left;">“RuntimeError:can not open CFlow file in line 338 of file ....\source\userapi\ThostFtdcUserApiImplBase.cpp” 报错是什么意思？</p><div class="region_panel" id="region_panel_2" style="display:block;"><table><tr><td>
<p>有core文件生成，调试后发现断点在CThostUserFlow::OpenFile中，可能是ulimit参数“open files”太小导致不能开启更多线程。</p>
</td></tr></table>
</div><p class="region_tail" id="region_tail_2" style="border-top-color:transparent;border-bottom-width:0;"></p></div></p>

<p>创建CThostFtdcMdApi实例。</p>
<span class="anchor" id="d22d43f6-bee1-4d40-8feb-1f7a3d70294e"></span>
## 1.函数原型
<p>static CThostFtdcMdApi *CreateFtdcMdApi(const char *pszFlowPath = "", const bool bIsUsingUdp=false, const bool bIsMulticast=false);</p>
<span class="anchor" id="fd8fec06-7c92-4283-a8fb-76549b8f86ab"></span>
## 2.参数
<p>pszFlowPath：常量字符指针，用于指定一个文件目录来存贮交易托管系统发布消息的状态。默认值代表当前目录。</p>
<p>bIsUsingUdp：是否使用UDP行情</p>
<p>bIsMulticast：是否使用组播行情</p>
<blockquote>
<p>组播行情只能在内网中使用，需要咨询所连接的系统是否支持组播行情。</p>
</blockquote>
<p>各类型行情字段组合如下：</p>
<table><tr><th style="TEXT-ALIGN: center;">　</th><th style="TEXT-ALIGN: center;">bIsUsingUdp</th><th style="TEXT-ALIGN: center;">bIsMulticast</th></tr><tr><td style="TEXT-ALIGN: left;">TCP行情前置</td>
<td style="TEXT-ALIGN: left;">false</td>
<td style="TEXT-ALIGN: left;">false</td>
</tr>
<tr><td style="TEXT-ALIGN: left;">UDP行情前置</td>
<td style="TEXT-ALIGN: left;">true</td>
<td style="TEXT-ALIGN: left;">false</td>
</tr>
<tr><td style="TEXT-ALIGN: left;">组播行情前置</td>
<td style="TEXT-ALIGN: left;">true</td>
<td style="TEXT-ALIGN: left;">true</td>
</tr>
</table>
<span class="anchor" id="de4e587c-9651-4e16-97c7-153d938ea246"></span>
## 3.返回
<p>返回一个CThostFtdcMdApi实例。</p>
<span class="anchor" id="022a5639-27f8-43ce-8cfd-d4b10a494002"></span>
## 4.调用示例
<pre><code>CThostFtdcMdApi  *pUserMdApi = CThostFtdcMdApi::CreateFtdcMdApi();
CSimpleMdHandler ash(pUserMdApi);
pUserMdApi-&gt;RegisterSpi(&amp;ash);
pUserMdApi-&gt;RegisterFront(“tcp://127.0.0.1:41205”);
pUserMdApi-&gt;Init();
</code></pre>
<span class="anchor" id="babbd108-e148-4da6-bc5b-6bff556cfb21"></span>
## 5.FAQ
<p><div class="region_i" id=""><p class="region_header" id="region_header_1" style="padding-left: 1em;font-weight : bold;text-indent: 0px;text-align: left;">“RuntimeError:can not open CFlow file in line 279 of file ....\source\userapi\ThostFtdcUserApiImplBase.cpp”程序一运行就报这个错是为什么？</p><div class="region_panel" id="region_panel_1" style="display:block;"><table><tr><td>
<p>程序运行之前，flow目录必须提前创建好，否则会报错。</p>
</td></tr></table>
</div><p class="region_tail" id="region_tail_1" style="border-top-color:transparent;border-bottom-width:0;"></p></div></p>

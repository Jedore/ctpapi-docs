<p>创建<a href="../_CTHOSTFTDCMDAPI/">CThostFtdcMdApi</a>实例。</p>
<span class="anchor" id="feef3132-922c-492f-bb07-f2f9c4ce71d6"></span>
## 1.函数原型
<p>static <a href="../_CTHOSTFTDCMDAPI/">CThostFtdcMdApi</a> *CreateFtdcMdApi(const char *pszFlowPath = "", const bool bIsUsingUdp=false, const bool bIsMulticast=false);</p>
<span class="anchor" id="0bc8866e-f599-403a-8a82-ee9bb4bad1d3"></span>
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
<p>连接mdfront时，在ini中有ThostChannelModel、ThostUsingMulticast两项用于配置对客户端的连接模式，分三种情况：</p>
<table><tr><th style="TEXT-ALIGN: center;">　</th><th style="TEXT-ALIGN: center;">ThostChannelModel</th><th style="TEXT-ALIGN: center;">ThostUsingMulticast</th><th style="TEXT-ALIGN: center;">终端配置的模式</th></tr><tr><td style="TEXT-ALIGN: left;">TCP模式</td>
<td style="TEXT-ALIGN: left;">tcp</td>
<td style="TEXT-ALIGN: left;">　</td>
<td style="TEXT-ALIGN: left;">TCP</td>
</tr>
<tr><td style="TEXT-ALIGN: left;">UDP模式</td>
<td style="TEXT-ALIGN: left;">udp</td>
<td style="TEXT-ALIGN: left;">no</td>
<td style="TEXT-ALIGN: left;">TCP、UDP</td>
</tr>
<tr><td style="TEXT-ALIGN: left;">组播模式</td>
<td style="TEXT-ALIGN: left;">udp</td>
<td style="TEXT-ALIGN: left;">yes</td>
<td style="TEXT-ALIGN: left;">组播</td>
</tr>
</table>
<span class="anchor" id="87be1d93-5970-4b6f-9f69-791cb3411bea"></span>
## 3.返回
<p>返回一个<a href="../_CTHOSTFTDCMDAPI/">CThostFtdcMdApi</a>实例。</p>
<span class="anchor" id="17bfeff0-4c50-48dc-931c-a7ce0dfb5938"></span>
## 4.调用示例
<pre><code>CThostFtdcMdApi  *pUserMdApi = CThostFtdcMdApi::CreateFtdcMdApi();
CSimpleMdHandler ash(pUserMdApi);
pUserMdApi-&gt;RegisterSpi(&amp;ash);
pUserMdApi-&gt;RegisterFront(“tcp://127.0.0.1:41205”);
pUserMdApi-&gt;Init();
</code></pre>
<span class="anchor" id="6f162c07-0c13-422d-83ba-c71947bc1cbc"></span>
## 5.FAQ
<p><div class="region_i"><p class="region_header" id="region_header_1" style="padding-left: 1em;font-weight : bold;text-indent: 0px;text-align: left;">“RuntimeError:can not open CFlow file in line 279 of file ....\source\userapi\ThostFtdcUserApiImplBase.cpp”程序一运行就报这个错是为什么？</p><div class="region_panel" id="region_panel_1" style="display:block;"><table><tr><td>
<p>程序运行之前，flow目录必须提前创建好，否则会报错。</p>
</td></tr></table>
</div><p class="region_tail" id="region_tail_1" style="border-top-color:transparent;border-bottom-width:0;"></p></div></p>

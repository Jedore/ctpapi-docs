<p>订阅行情，对应响应<a href="../../CTHOSTFTDCMDSPI/ONRSPSUBMARKETDATA/">OnRspSubMarketData</a>；订阅成功后，通过<a href="../../CTHOSTFTDCMDSPI/ONRTNDEPTHMARKETDATA/">OnRtnDepthMarketData</a>推送行情信息。</p>
<blockquote>
<p>订阅全市场合约需要把全市场合约代码都赋值给ppInstrumentID，填空不能订阅全市场合约。</p>
<p>目前<a href="../../CTHOSTFTDCMDSPI/ONRTNDEPTHMARKETDATA/">OnRtnDepthMarketData</a>响应的数量会比请求合约的数量少，且<a href="../../CTHOSTFTDCMDSPI/ONRTNDEPTHMARKETDATA/">OnRtnDepthMarketData</a>响应中会有多次bIsLast=true，此为已知问题，但不影响实际订阅的合约数量。</p>
</blockquote>
<span class="anchor" id="11ffa01c-de5e-4e93-b944-9dcf709fa80c"></span>
## 1.函数原型
<p>virtual int SubscribeMarketData(char *ppInstrumentID[], int nCount) = 0;</p>
<span class="anchor" id="b4e32c6c-65fe-4cb1-ac83-6264e57b3433"></span>
## 2.参数
<p>ppInstrumentID：合约数组</p>
<p>nCount：合约数组的数量</p>
<span class="anchor" id="9b882dc3-a424-4d30-b982-4b3d7d209c80"></span>
## 3.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="a8b3077e-afec-4c99-b716-baa7b321e934"></span>
## 4.调用示例
<pre><code>char **ppInstrumentID = new char*[50];
ppInstrumentID[0] = "T1712";
m_pUserMdApi-&gt;SubscribeMarketData(ppInstrumentID, 1);
</code></pre>
<span class="anchor" id="c4726761-e79e-4c26-ad2e-6307739d22c6"></span>
## 5.FAQ
<p><div class="region_i"><p class="region_header" id="region_header_1" style="padding-left: 1em;font-weight : bold;text-indent: 0px;text-align: left;">能否订阅重收全天的行情？</p><div class="region_panel" id="region_panel_1" style="display:block;"><table><tr><td>
<p>不行，只推送最新的行情。</p>
</td></tr></table>
</div><p class="region_tail" id="region_tail_1" style="border-top-color:transparent;border-bottom-width:0;"></p></div></p>
<p><span alt="" id="anchor-id-01"></span> </p>
<p><div class="region_i"><p class="region_header" id="region_header_2" style="padding-left: 1em;font-weight : bold;text-indent: 0px;text-align: left;">订阅全部合约包含期货和期权所有合约后，发生OnSessionDisconnected（4097）的报错，是什么原因？</p><div class="region_panel" id="region_panel_2" style="display:block;"><table><tr><td>
<p>行情前置有个缓冲区限制，一瞬间发送太多超出缓冲区后就会有触发自我保护机制把session断开，可以尝试分批订阅，比如每订阅1000个延迟1秒。</p>
</td></tr></table>
</div><p class="region_tail" id="region_tail_2" style="border-top-color:transparent;border-bottom-width:0;"></p></div></p>

<p>订阅行情，对应响应<a href="../../CTHOSTFTDCMDSPI/ONRSPSUBMARKETDATA/">OnRspSubMarketData</a>；订阅成功后，通过<a href="../../CTHOSTFTDCMDSPI/ONRTNDEPTHMARKETDATA/">OnRtnDepthMarketData</a>推送行情信息。</p>
<blockquote>
<p>订阅全市场合约需要把全市场合约代码都赋值给ppInstrumentID，填空不能订阅全市场合约。</p>
</blockquote>
<span class="anchor" id="ecda8f8d-8326-4402-a7b7-3e07e3ec62f6"></span>
## 1.函数原型
<p>virtual int SubscribeMarketData(char *ppInstrumentID[], int nCount) = 0;</p>
<span class="anchor" id="1ba52bbf-0f54-4bf1-9128-a6eeef2179b1"></span>
## 2.参数
<p>ppInstrumentID：合约数组</p>
<p>nCount：合约数组的数量</p>
<span class="anchor" id="e51070b3-181e-4465-b4d2-cebcb72f1006"></span>
## 3.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="5f1cf3f6-f437-4695-8127-d397effa54a1"></span>
## 4.调用示例
<pre><code>char **ppInstrumentID = new char*[50];
ppInstrumentID[0] = "T1712";
m_pUserMdApi-&gt;SubscribeMarketData(ppInstrumentID, 1);
</code></pre>
<span class="anchor" id="0d2e7a8d-df19-4ffb-8445-ea736dd8474b"></span>
## 5.FAQ
<p><div class="region_i"><p class="region_header" id="region_header_1" style="padding-left: 1em;font-weight : bold;text-indent: 0px;text-align: left;">能否订阅重收全天的行情？</p><div class="region_panel" id="region_panel_1" style="display:block;"><table><tr><td>
<p>不行，只推送最新的行情。</p>
</td></tr></table>
</div><p class="region_tail" id="region_tail_1" style="border-top-color:transparent;border-bottom-width:0;"></p></div></p>

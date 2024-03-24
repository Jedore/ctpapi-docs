<p>订阅行情，对应响应<a href="../../CTHOSTFTDCMDSPI/ONRSPSUBMARKETDATA/">OnRspSubMarketData</a>；订阅成功后，通过<a href="../../CTHOSTFTDCMDSPI/ONRTNDEPTHMARKETDATA/">OnRtnDepthMarketData</a>推送行情信息。</p>
<blockquote>
<p>订阅全市场合约需要把全市场合约代码都赋值给ppInstrumentID，填空不能订阅全市场合约。</p>
<p>目前<a href="../../CTHOSTFTDCMDSPI/ONRTNDEPTHMARKETDATA/">OnRtnDepthMarketData</a>响应的数量会比请求合约的数量少，且<a href="../../CTHOSTFTDCMDSPI/ONRTNDEPTHMARKETDATA/">OnRtnDepthMarketData</a>响应中会有多次bIsLast=true，此为已知问题，但不影响实际订阅的合约数量。</p>
</blockquote>
<span class="anchor" id="c75bb1f0-71f9-4402-a3c0-9026356c413a"></span>
## 1.函数原型
<p>virtual int SubscribeMarketData(char *ppInstrumentID[], int nCount) = 0;</p>
<span class="anchor" id="2d8ad0ef-4f16-4d3e-9897-a4300aeba524"></span>
## 2.参数
<p>ppInstrumentID：合约数组</p>
<p>nCount：合约数组的数量</p>
<span class="anchor" id="966c5fb5-37c6-49c6-b3f5-0e617ce3526b"></span>
## 3.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="60591551-28e0-45f2-91e1-29dfff473826"></span>
## 4.调用示例
<pre><code>char **ppInstrumentID = new char*[50];
ppInstrumentID[0] = "T1712";
m_pUserMdApi-&gt;SubscribeMarketData(ppInstrumentID, 1);
</code></pre>
<span class="anchor" id="a80e2ff0-ce80-43ac-af65-8045735549f4"></span>
## 5.FAQ
<p><div class="region_i"><p class="region_header" id="region_header_1" style="padding-left: 1em;font-weight : bold;text-indent: 0px;text-align: left;">能否订阅重收全天的行情？</p><div class="region_panel" id="region_panel_1" style="display:block;"><table><tr><td>
<p>不行，只推送最新的行情。</p>
</td></tr></table>
</div><p class="region_tail" id="region_tail_1" style="border-top-color:transparent;border-bottom-width:0;"></p></div></p>

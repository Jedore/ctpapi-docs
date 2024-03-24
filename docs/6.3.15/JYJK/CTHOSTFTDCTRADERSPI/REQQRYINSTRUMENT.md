<p>请求查询合约，填空可以查询到所有合约。</p>
<p>响应:OnRspQryInstrument</p>
<span class="anchor" id="e822d211-dec6-4e66-8202-5aef13b90681"></span>
## 1.函数原型
<p>virtual int ReqQryInstrument(CThostFtdcQryInstrumentField *pQryInstrument, int nRequestID) = 0;</p>
<span class="anchor" id="0dd742cd-f023-4fcf-8792-93c1545f8a9e"></span>
## 2.参数
<p>pQryInstrument：查询合约</p>
<pre><code>struct CThostFtdcQryInstrumentField
{
    ///合约代码
    TThostFtdcInstrumentIDType InstrumentID;
    ///交易所代码
    TThostFtdcExchangeIDType ExchangeID;
    ///合约在交易所的代码
    TThostFtdcExchangeInstIDType ExchangeInstID;
    ///产品代码
    TThostFtdcInstrumentIDType ProductID;
};
</code></pre>
<p>nRequestID：请求ID，对应响应里的nRequestID，无递增规则，由用户自行维护。</p>
<span class="anchor" id="dcd2ff1e-ff18-4204-a137-187526661cb8"></span>
## 3.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="c6bfca00-44b8-4548-9d8a-5a5ac3830434"></span>
## 4.调用示例
<pre><code>CThostFtdcQryInstrumentField a = { 0 };
strcpy_s(a.InstrumentID, "rb1809");
strcpy_s(a.ExchangeID, "SHFE");
m_pUserApi-&gt;ReqQryInstrument(&amp;a, nRequestID++);
</code></pre>
<span class="anchor" id="a21b7ff0-5f0f-400d-9f68-88af6bb1a673"></span>
## 5.FAQ
<p><div class="region_i" id=""><p class="region_header" id="region_header_1" style="padding-left: 1em;font-weight : bold;text-indent: 0px;text-align: left;">为何查询不到郑商所跨式和宽跨式套利合约？</p><div class="region_panel" id="region_panel_1" style="display:block;"><table><tr><td>
<p>郑商所没有推跨式和宽跨式套利合约，所以查询不到此类合约。</p>
</td></tr></table>
</div><p class="region_tail" id="region_tail_1" style="border-top-color:transparent;border-bottom-width:0;"></p></div></p>

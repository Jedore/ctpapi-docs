<p>请求查询合约，填空可以查询到所有合约。</p>
<p>响应:OnRspQryInstrument</p>
<span class="anchor" id="619270fb-ec06-4120-82af-88b930de6c27"></span>
## 1.函数原型
<p>virtual int ReqQryInstrument(CThostFtdcQryInstrumentField *pQryInstrument, int nRequestID) = 0;</p>
<span class="anchor" id="3a9f07ad-6ee4-4c00-ba7d-d53a00bd611a"></span>
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
<span class="anchor" id="ea2961be-e0a6-4506-96ea-c4f4f83b4020"></span>
## 3.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="f4487ba9-ca95-41fc-a982-d55a706eb006"></span>
## 4.调用示例
<pre><code>CThostFtdcQryInstrumentField a = { 0 };
strcpy_s(a.InstrumentID, "rb1809");
strcpy_s(a.ExchangeID, "SHFE");
m_pUserApi-&gt;ReqQryInstrument(&amp;a, nRequestID++);
</code></pre>
<span class="anchor" id="44bda26a-74b7-4b49-aad6-73cbfcc740d1"></span>
## 5.FAQ
<p><div class="region_i" id=""><p class="region_header" id="region_header_1" style="padding-left: 1em;font-weight : bold;text-indent: 0px;text-align: left;">为何查询不到郑商所跨式和宽跨式套利合约？</p><div class="region_panel" id="region_panel_1" style="display:block;"><table><tr><td>
<p>郑商所没有推跨式和宽跨式套利合约，所以查询不到此类合约。</p>
</td></tr></table>
</div><p class="region_tail" id="region_tail_1" style="border-top-color:transparent;border-bottom-width:0;"></p></div></p>

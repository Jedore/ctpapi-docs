<p>请求查询投资者持仓明细</p>
<p>响应: OnRspQryInvestorPositionCombineDetail</p>
<span class="anchor" id="ec6fdfb8-d3f1-4906-b1f7-3a2fa63d88f1"></span>
## 1.函数原型
<p>virtual int ReqQryInvestorPositionCombineDetail(CThostFtdcQryInvestorPositionCombineDetailField *pQryInvestorPositionCombineDetail, int nRequestID) = 0;</p>
<span class="anchor" id="18541ead-1f5e-419e-b9da-538cf94cd49c"></span>
## 2.参数
<p>pQryInvestorPositionCombineDetail：查询组合持仓明细</p>
<pre><code>struct CThostFtdcQryInvestorPositionCombineDetailField
{
    ///经纪公司代码
    TThostFtdcBrokerIDType BrokerID;
    ///投资者代码
    TThostFtdcInvestorIDType InvestorID;
    ///组合持仓合约编码
    TThostFtdcInstrumentIDType CombInstrumentID;
    ///交易所代码
    TThostFtdcExchangeIDType ExchangeID;
    ///投资单元代码
    TThostFtdcInvestUnitIDType InvestUnitID;
};
</code></pre>
<p>nRequestID：请求ID，对应响应里的nRequestID，无递增规则，由用户自行维护。</p>
<span class="anchor" id="76655313-d9f2-4080-b70e-4184951b7f81"></span>
## 3.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="0e43f229-14be-42f0-b284-d314355c11ed"></span>
## 4.调用示例
<p>无</p>
<span class="anchor" id="544267b4-73df-4ba8-98ac-e3c9d48fae6e"></span>
## 5.FAQ
<p>无</p>

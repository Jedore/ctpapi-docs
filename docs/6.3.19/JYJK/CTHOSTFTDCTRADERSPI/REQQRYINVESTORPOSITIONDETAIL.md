<p>请求查询投资者持仓明细，对应响应OnRspQryInvestorPositionDetail。</p>
<p>CTP系统根据来自交易所的成交记录生成持仓明细记录，一笔成交记录对应一条持仓明细记录。</p>
<span class="anchor" id="dceef0d1-7585-409f-b4b4-bd3556b96c4f"></span>
## 1.函数原型
<p>virtual int ReqQryInvestorPositionDetail(CThostFtdcQryInvestorPositionDetailField *pQryInvestorPositionDetail, int nRequestID) = 0;</p>
<span class="anchor" id="d7efcf61-7c8f-40f8-97e2-be3d7f512119"></span>
## 2.参数
<p>pQryInvestorPositionDetail：查询投资者持仓明细</p>
<pre><code>struct CThostFtdcQryInvestorPositionDetailField
{
    ///经纪公司代码
    TThostFtdcBrokerIDType BrokerID;
    ///投资者代码
    TThostFtdcInvestorIDType InvestorID;
    ///合约代码
    TThostFtdcInstrumentIDType InstrumentID;
    ///交易所代码
    TThostFtdcExchangeIDType ExchangeID;
    ///投资单元代码
    TThostFtdcInvestUnitIDType InvestUnitID;
};
</code></pre>
<p>nRequestID：请求ID，对应响应里的nRequestID，无递增规则，由用户自行维护。</p>
<span class="anchor" id="5eadfa1e-303d-4629-bbdf-4f9653498caf"></span>
## 3.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="adbee836-06e3-4d7a-8317-8b58608813c7"></span>
## 4.调用示例
<p>无</p>
<span class="anchor" id="dc7efd88-c5d5-4f18-bf9e-baa4118b6eaf"></span>
## 5.FAQ
<p>无</p>

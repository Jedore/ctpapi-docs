<p>请求查询做市商合约手续费率响应，当执行<a href="../../CTHOSTFTDCTRADERSPI/REQQRYMMINSTRUMENTCOMMISSIONRATE/">ReqQryMMInstrumentCommissionRate</a>后，该方法被调用。</p>
<span class="anchor" id="859fe3c1-9d57-47db-8ea7-3a869dba06d8"></span>
## 1.函数原型
<p>virtual void OnRspQryMMInstrumentCommissionRate(CThostFtdcMMInstrumentCommissionRateField *pMMInstrumentCommissionRate, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="d39d9388-65db-473e-9fe0-e9c9840082ea"></span>
## 2.参数
<p>pMMInstrumentCommissionRate：做市商合约手续费率</p>
<pre><code>struct CThostFtdcMMInstrumentCommissionRateField
{
    ///保留的无效字段
    TThostFtdcOldInstrumentIDType   reserve1;
    ///投资者范围
    TThostFtdcInvestorRangeType InvestorRange;
    ///经纪公司代码
    TThostFtdcBrokerIDType  BrokerID;
    ///投资者代码
    TThostFtdcInvestorIDType    InvestorID;
    ///开仓手续费率
    TThostFtdcRatioType OpenRatioByMoney;
    ///开仓手续费
    TThostFtdcRatioType OpenRatioByVolume;
    ///平仓手续费率
    TThostFtdcRatioType CloseRatioByMoney;
    ///平仓手续费
    TThostFtdcRatioType CloseRatioByVolume;
    ///平今手续费率
    TThostFtdcRatioType CloseTodayRatioByMoney;
    ///平今手续费
    TThostFtdcRatioType CloseTodayRatioByVolume;
    ///合约代码
    TThostFtdcInstrumentIDType  InstrumentID;
};
</code></pre>
<p>pRspInfo：响应信息</p>
<pre><code>struct CThostFtdcRspInfoField
{
    ///错误代码
    TThostFtdcErrorIDType ErrorID;
    ///错误信息
    TThostFtdcErrorMsgType ErrorMsg;
};
</code></pre>
<p>nRequestID：返回用户操作请求的ID，该ID 由用户在操作请求时指定。</p>
<p>bIsLast：指示该次返回是否为针对nRequestID的最后一次返回。</p>
<span class="anchor" id="becffe85-ea2d-4820-8d34-0cb46b26f776"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="24bc267c-3706-4116-90ed-1ceac937e68a"></span>
## 4.FAQ
<p>无</p>

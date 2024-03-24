<p>请求查询做市商期权合约手续费响应，当执行ReqQryMMOptionInstrCommRate后，该方法被调用。</p>
<span class="anchor" id="c56a95c0-9b83-4ae0-a648-060c0e4d1113"></span>
## 1.函数原型
<p>virtual void OnRspQryMMOptionInstrCommRate(CThostFtdcMMOptionInstrCommRateField *pMMOptionInstrCommRate, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="02a0dca2-4fb8-48f9-8e10-fe8bc0715139"></span>
## 2.参数
<p>pMMOptionInstrCommRate：当前做市商期权合约手续费的详细内容</p>
<pre><code>struct CThostFtdcMMOptionInstrCommRateField
{
    ///合约代码
    TThostFtdcInstrumentIDType InstrumentID;
    ///投资者范围
    TThostFtdcInvestorRangeType InvestorRange;
    ///经纪公司代码
    TThostFtdcBrokerIDType BrokerID;
    ///投资者代码
    TThostFtdcInvestorIDType InvestorID;
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
    ///执行手续费率
    TThostFtdcRatioType StrikeRatioByMoney;
    ///执行手续费
    TThostFtdcRatioType StrikeRatioByVolume;
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
<span class="anchor" id="b5a7be7e-f849-4e2d-bef5-76091e8e4a13"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="bf11f89d-6ce1-4132-a9c0-99e8a775ac0b"></span>
## 4.FAQ
<p>无</p>

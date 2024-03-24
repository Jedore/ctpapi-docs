<p>请求查询做市商合约手续费率响应，当执行<a href="../../CTHOSTFTDCTRADERSPI/REQQRYMMINSTRUMENTCOMMISSIONRATE/">ReqQryMMInstrumentCommissionRate</a>后，该方法被调用。</p>
<span class="anchor" id="b3c858e5-e8d6-43c4-a3d4-8c0f2fbade58"></span>
## 1.函数原型
<p>virtual void OnRspQryMMInstrumentCommissionRate(CThostFtdcMMInstrumentCommissionRateField *pMMInstrumentCommissionRate, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="12c5d583-3ddc-4b88-bc36-584ac2d1d842"></span>
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
<span class="anchor" id="193256cf-69d1-4dba-acbe-6b2f627dc068"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="77ba55de-a991-4e69-bd83-5eb9f1240e3b"></span>
## 4.FAQ
<p>无</p>

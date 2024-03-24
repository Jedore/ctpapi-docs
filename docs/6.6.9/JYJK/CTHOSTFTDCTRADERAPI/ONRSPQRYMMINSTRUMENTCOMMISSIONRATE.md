<p>请求查询做市商合约手续费率响应，当执行<a href="../../CTHOSTFTDCTRADERSPI/REQQRYMMINSTRUMENTCOMMISSIONRATE/">ReqQryMMInstrumentCommissionRate</a>后，该方法被调用。</p>
<span class="anchor" id="6fa844f1-c506-44a8-88f9-bc30604c1f16"></span>
## 1.函数原型
<p>virtual void OnRspQryMMInstrumentCommissionRate(CThostFtdcMMInstrumentCommissionRateField *pMMInstrumentCommissionRate, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="d5fc2182-2371-4252-87cd-9665d9db8c18"></span>
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
<span class="anchor" id="ae409360-2dd4-4b2e-b8f6-a0533674faf7"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="82727c35-3645-4a2c-97aa-b6f77e182ffc"></span>
## 4.FAQ
<p>无</p>

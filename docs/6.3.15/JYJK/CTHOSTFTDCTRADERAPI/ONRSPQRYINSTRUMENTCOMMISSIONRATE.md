<p>请求查询合约手续费率响应，当执行ReqQryInstrumentCommissionRate后，该方法被调用。</p>
<span class="anchor" id="20a86658-d800-456f-91d6-37028b3a46cc"></span>
## 1.函数原型
<p>virtual void OnRspQryInstrumentCommissionRate(CThostFtdcInstrumentCommissionRateField *pInstrumentCommissionRate, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="842a4cb1-c33b-40b5-af0a-82153a19a320"></span>
## 2.参数
<p>pInstrumentCommissionRate：合约手续费率</p>
<pre><code>struct CThostFtdcInstrumentCommissionRateField
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
    ///交易所代码
    TThostFtdcExchangeIDType ExchangeID;
    ///业务类型
    TThostFtdcBizTypeType BizType;
    ///投资单元代码
    TThostFtdcInvestUnitIDType InvestUnitID;
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
<span class="anchor" id="d9e6af19-566b-4057-9164-0ced4b34c1f5"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="fb91da94-668d-405f-a443-1f53fbe9d210"></span>
## 4.FAQ
<p>无</p>

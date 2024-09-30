<p>查询最大报单数量响应，当执行<a href="../../CTHOSTFTDCTRADERSPI/REQQUERYMAXORDERVOLUME/">ReqQryMaxOrderVolume</a>后，该方法被调用。</p>
<span class="anchor" id="c9208393-4321-41b4-b4eb-5ca92f5ac6e9"></span>
## 1.函数原型
<p>virtual void OnRspQryMaxOrderVolume(CThostFtdcQryMaxOrderVolumeField *pQryMaxOrderVolume, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="845eaab8-eba0-45dd-859b-45f5640c6675"></span>
## 2.参数
<p>pQryMaxOrderVolume：查询最大报单数量</p>
<pre><code>struct CThostFtdcQryMaxOrderVolumeField
{
    ///经纪公司代码
    TThostFtdcBrokerIDType BrokerID;
    ///投资者代码
    TThostFtdcInvestorIDType InvestorID;
    ///保留的无效字段
    TThostFtdcOldInstrumentIDType   reserve1;
    ///合约代码
    TThostFtdcInstrumentIDType InstrumentID;
    ///买卖方向
    TThostFtdcDirectionType Direction;
    ///开平标志
    TThostFtdcOffsetFlagType OffsetFlag;
    ///投机套保标志
    TThostFtdcHedgeFlagType HedgeFlag;
    ///最大允许报单数量
    TThostFtdcVolumeType MaxVolume;
    ///交易所代码
    TThostFtdcExchangeIDType ExchangeID;
    ///投资单元代码
    TThostFtdcInvestUnitIDType InvestUnitID;
};
</code></pre>
<p>MaxVolume：取值结果为，min（可开/可平，限价单最大下单量）；可开根据昨结算价计算得出。</p>
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
<span class="anchor" id="ec62ac40-f048-408d-8605-740a481f5472"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="67e9fffa-dc7a-4f53-9f4e-f8b1fa370ac3"></span>
## 4.FAQ
<p>无</p>

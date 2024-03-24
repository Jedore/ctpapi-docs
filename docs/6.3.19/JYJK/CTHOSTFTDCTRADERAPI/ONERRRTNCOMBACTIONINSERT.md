<span class="anchor" id="42f8014d-c7d3-4a5c-8055-d28cad764454"></span>
## 1.说明
<p>申请组合录入错误回报</p>
<span class="anchor" id="fe0520c0-5562-45b8-883a-db3024723d62"></span>
## 2.函数原型
<p>virtual void OnErrRtnCombActionInsert(CThostFtdcInputCombActionField *pInputCombAction, CThostFtdcRspInfoField *pRspInfo) {};</p>
<span class="anchor" id="67a8cd3f-51f0-4338-b46a-780496d3e8cc"></span>
## 3.参数
<p>pInputCombAction：输入的申请组合</p>
<pre><code>struct CThostFtdcInputCombActionField
{
    ///经纪公司代码
    TThostFtdcBrokerIDType BrokerID;
    ///投资者代码
    TThostFtdcInvestorIDType InvestorID;
    ///合约代码
    TThostFtdcInstrumentIDType InstrumentID;
    ///组合引用
    TThostFtdcOrderRefType CombActionRef;
    ///用户代码
    TThostFtdcUserIDType UserID;
    ///买卖方向
    TThostFtdcDirectionType Direction;
    ///数量
    TThostFtdcVolumeType Volume;
    ///组合指令方向
    TThostFtdcCombDirectionType CombDirection;
    ///投机套保标志
    TThostFtdcHedgeFlagType HedgeFlag;
    ///交易所代码
    TThostFtdcExchangeIDType ExchangeID;
    ///IP地址
    TThostFtdcIPAddressType IPAddress;
    ///Mac地址
    TThostFtdcMacAddressType MacAddress;
    ///投资单元代码
    TThostFtdcInvestUnitIDType InvestUnitID;
    ///前置编号
    TThostFtdcFrontIDType   FrontID;
    ///会话编号
    TThostFtdcSessionIDType SessionID;
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
<span class="anchor" id="6535aac7-4039-4b6c-961c-544066940ad5"></span>
## 4.返回
<p>无</p>
<span class="anchor" id="33cedc5e-6f50-453e-ad6c-80e72d925d6d"></span>
## 5.FAQ
<p>无</p>

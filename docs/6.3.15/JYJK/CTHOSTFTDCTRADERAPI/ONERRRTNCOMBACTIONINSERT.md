<span class="anchor" id="791621b4-ab15-405a-beac-7f99f63ac9f8"></span>
## 1.说明
<p>申请组合录入错误回报</p>
<span class="anchor" id="29204fd6-9d1e-4856-900d-0b9ef4f64310"></span>
## 2.函数原型
<p>virtual void OnErrRtnCombActionInsert(CThostFtdcInputCombActionField *pInputCombAction, CThostFtdcRspInfoField *pRspInfo) {};</p>
<span class="anchor" id="19a8a718-d024-4c54-88c1-b7bd99a07177"></span>
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
<span class="anchor" id="dbed17c6-dfb6-4381-8546-bae3eeaad0f0"></span>
## 4.返回
<p>无</p>
<span class="anchor" id="69acff49-cf3a-4026-a2b9-40b20836abc5"></span>
## 5.FAQ
<p>无</p>

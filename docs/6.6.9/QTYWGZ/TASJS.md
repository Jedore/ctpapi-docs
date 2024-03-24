<p>本文旨在介绍CTP API中与TAS（Trading at Settlement, TAS 盘中结算价交易机制）业务相关的内容，具体交易细则请参考交易所官方文档。</p>
<span class="anchor" id="1b1acdac-1f00-4f46-83b9-91a0d6e98a87"></span>
## 1. 报单
<p>接口名称：<a href="../../JYJK/CTHOSTFTDCTRADERSPI/REQORDERINSERT/">ReqOrderInsert</a></p>
<ol>
<li><p>合约（InstrumentID）：填写TAS合约，如对sc1901进行TAS交易，则合约填写sc1911TAS</p></li>
<li><p>价格（LimitPrice）：必须为0。</p></li>
<li><p>类型（OrderPriceType）：只支持限价指令THOST_FTDC_OPT_LimitPrice。</p></li>
</ol>
<p>其余字段与标的期货对应字段意义相同（买卖方向、平今平昨、投机套保等字段都需填写）。</p>
<p>TAS开仓，盘中成交后直接计入期货持仓；TAS平仓区分平今/平昨，平对应的期货持仓；平仓的仓位冻结按照标的合约进行冻结。</p>
<span class="anchor" id="451ddffb-ddc6-4971-87cf-a15ed15d408a"></span>
## 2. 成交
<p>接口名称：<a href="../../JYJK/CTHOSTFTDCTRADERAPI/ONRTNTRADE/">OnRtnTrade</a></p>
<ol>
<li><p>交易成交类型(TradeType)：为普通成交THOST_FTDC_TRDT_Common。</p></li>
<li><p>成交价（Price）：对于TAS成交，成交价无意义。</p></li>
</ol>
<span class="anchor" id="d40a9026-d4e0-4af0-bd7c-e4b5eeda759c"></span>
## 3. 持仓
<p>接口名称：<a href="../../JYJK/CTHOSTFTDCTRADERAPI/ONRSPQRYINVESTORPOSITIONDETAIL/">OnRspQryInvestorPositionDetail</a></p>
<ol>
<li>持仓明细新增字段特殊持仓标志（SpecPosiType）：标识该明细为tas衍生成交。</li>
</ol>
<p>接口名称：<a href="../../JYJK/CTHOSTFTDCTRADERAPI/ONRSPQRYINVESTORPOSITION/">OnRspQryInvestorPosition</a></p>
<ol>
<li><p>持仓汇总新增字段tas持仓手数（TasPosition）：记录该汇总中TAS开仓的数量。</p></li>
<li><p>持仓汇总新增字段tas持仓成本（TasPositionCost）：记录该汇总中TAS持仓成本。</p></li>
</ol>
<p>tas只有当天有效，不计入昨仓。结算完就变成标的持仓了，不再是tas合约持仓。可以理解成标的合约的昨持仓。</p>
<span class="anchor" id="e7b48e4e-fea6-4896-b87e-aa0b248c0fdc"></span>
## 4. 手续费和保证金
<p>开仓保证金和手续费冻结都按照标的合约停板价冻结。</p>
<p>实收保证金率和手续费率都按照标的合约计算。</p>
<p>保证金率和手续费率使用标的合约的费率，通过费率查询接口只能查询到标的合约的费率。</p>
<span class="anchor" id="7520ac34-01ea-4666-aa86-f32d0c2a4b46"></span>
## 5. 盈亏
<p>计算持仓盈亏的时候，对于(总数量-TAS数量)部分计算持仓盈亏和保证金。对于TAS数量不计算盈亏。</p>
<span class="anchor" id="6b0b1163-38e7-4a96-9f26-39ec68a738b7"></span>
## 6.合约行情
<p>合约代码、合约状态、买卖方向、报单量、成交量、日期、时间等字段正常发布。其余字段无意义，均为空。</p>
<p>盘中TAS成交量、成交额不计入标的合约的成交量、成交额。</p>
<span class="anchor" id="e988c8eb-d05a-40e3-b999-6a057a267428"></span>
## 7.代码示例
<pre><code>void orderinsert()
{
    CThostFtdcInputOrderField t = { 0 };
    strcpy_s(t.BrokerID, "1007");
    strcpy_s(t.InvestorID, "10000001");
    strcpy_s(t.UserID, "10000001");
    t.Direction = THOST_FTDC_D_Sell;
    t.CombOffsetFlag[0] = THOST_FTDC_OF_Open;
    t.CombHedgeFlag[0] = THOST_FTDC_HF_Speculation;
    t.ContingentCondition = THOST_FTDC_CC_Immediately;
    strcpy_s(t.InstrumentID, "sc2006TAS");  //tas合约代码
    t.ForceCloseReason = THOST_FTDC_FCC_NotForceClose;;
    t.LimitPrice = 0;   //价格为0
    t.StopPrice = 0;
    t.OrderPriceType = THOST_FTDC_OPT_LimitPrice;
    t.VolumeCondition = THOST_FTDC_VC_AV;
    t.TimeCondition = THOST_FTDC_TC_GFD;
    t.VolumeTotalOriginal = 10;
    m_ptraderapi-&gt;ReqOrderInsert(&amp;t, m_requestid++);
}
</code></pre>
